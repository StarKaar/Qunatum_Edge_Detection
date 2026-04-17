import cv2 as cv
import qiskit
from src.config import get_backend
from src.image_utilities import pad_to_quantum_image, initialize_state_vector
from src.quantum_engine import build_edge_circuit
from qiskit import transpile
from qiskit_ibm_runtime import Sampler

img = cv.imread('Pictures/diag.jpg', cv.IMREAD_GRAYSCALE)

padded_image = pad_to_quantum_image(img)
image_mask = padded_image.flatten()
total_pixels = len(image_mask)

initial_state = initialize_state_vector(total_pixels)
masked_state = initial_state * image_mask

norm = np.linalg.norm(masked_state)
if norm > 0:
    final_state = masked_state / norm
else:
    raise ValueError("The image mask was completely black; state annihilated.")


probabilities = np.abs(final_state)**2
probabilities_flat = probabilities.flatten().real

backend = get_backend()
qc = build_edge_circuit(final_state)
transpiled_qc=transpile(qc,backend)
sampler = Sampler(mode=backend)
result = sampler.run([transpiled_qc], shots=100000).result()

counts = result[0].data.meas.get_counts()
print(f"Measurement results: {counts}")