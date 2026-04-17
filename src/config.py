from qiskit_ibm_runtime import QiskitRuntimeService

def get_backend():
    
    token = "bWWllLM0ZCJh8mSUh-WVCWhOVrIUdHaiInTP1mKHys0e" 
    service = QiskitRuntimeService(channel="ibm_quantum_platform", token=token)
    return service.least_busy(simulator=False)