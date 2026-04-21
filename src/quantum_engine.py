from qiskit import QuantumCircuit
from qiskit.circuit.library import StatePreparation

from qiskit import QuantumCircuit
from qiskit.circuit.library import StatePreparation

def build_edge_circuit(final_state, num_qubits=16):
    state_prep = StatePreparation(final_state)
    qc = QuantumCircuit(num_qubits)
    qc.append(state_prep, range(num_qubits))
    qc.barrier()
    qc.h(0)
    qc.measure_all()
    return qc
