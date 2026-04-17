from qiskit_ibm_runtime import QiskitRuntimeService

def get_backend():
    
    token = "Your Token here" 
    service = QiskitRuntimeService(channel="ibm_quantum_platform", token=token)
    return service.least_busy(simulator=False)
