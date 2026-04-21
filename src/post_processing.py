import matplotlib.pyplot as plt
from image_utilities import padded_image
from main import total_pixels, probabilities_flat, initial_state, final_state, result, qc
from qiskit.visualization import plot_histogram
import math
import numpy as np


plt.figure(figsize=(12, 6))

#The Padded Image Mask
plt.subplot(1, 2, 1)
plt.imshow(padded_image, cmap='gray')
plt.title(f"Padded Image Mask\n({total_pixels} pixels)")

# The Quantum State Probabilities
plt.subplot(1, 2, 2)
# We won't label all 32+ states on the X-axis as it gets crowded, just use ranges
x_indices = np.arange(total_pixels)
plt.bar(x_indices, probabilities_flat, width=0.3)
plt.title("Post-Measurement Probability Distribution")
plt.xlabel("Computational Basis State Index")
plt.ylabel("Probability")

plt.tight_layout()
plt.show()

try:
    plt.show()
except Exception as e:
    pass # Silently catch the GUI crash when the window closes

print(f"Total Qubits Simulated: {int(math.log2(total_pixels))}")
print(f"Total Pixels (States): {total_pixels}")
print(f"Sum of all probabilities (should be 1.0): {np.sum(probabilities_flat):.4f}")
print(initial_state)
print(final_state)

counts = result[0].data.meas.get_counts()
print(f"Measurement results: {counts}")


qc.draw(output="mpl")
plot_histogram(counts)
plt.show()

#Detecting edges based on measurement counts
n = int(math.log2(total_pixels))

full_counts = {}
for i in range(total_pixels):
    # Convert number to bitstring (e.g., 2 -> '010')
    bitstring = format(i, f'0{n}b')
    
    # Check if we measured this state
    if bitstring in counts:
        val = counts[bitstring]
    else:
        val = 0
        
    full_counts[bitstring] = val

print(full_counts)

counts_arr=[]
for i in range(total_pixels):
    bitstring=format(i,f'0{n}b')
    counts_arr.append(full_counts[bitstring])

print(counts_arr)

even_count_arr=[]
for i in range(1,total_pixels,2):
    even_count_arr.append(counts_arr[i])

print(even_count_arr)

threshold_value = np.average(even_count_arr)

edge_det_arr=[]
for i in range(0,int(total_pixels/2)):
    if even_count_arr[i]>threshold_value:
        edge_det_arr.append(1)
    else:
        edge_det_arr.append(0)

print(edge_det_arr)

# Marking the boundary

original_shape = padded_image.shape
flattened = padded_image.flatten()

for i in range(len(edge_det_arr)):
    if edge_det_arr[i] == 1:
        if flattened[2*i] > flattened[2*i+1]:
            flattened[2*i] = 255
            flattened[2*i+1] = 0
        elif flattened[2*i] < flattened[2*i+1]:
            flattened[2*i] = 0
            flattened[2*i+1] = 255
    elif edge_det_arr[i] == 0:
        flattened[2*i] = 255
        flattened[2*i+1] = 255

reshaped_image = flattened.reshape(original_shape)
plt.imshow(reshaped_image, cmap='gray')
plt.title("Edge Detection Result")
plt.show()
