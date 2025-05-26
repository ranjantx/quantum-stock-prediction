# test_import.py
from qiskit_ibm_runtime import QiskitRuntimeService

# Initialize the service
service = QiskitRuntimeService(
    channel="ibm_quantum",
    token="9ad7e3042518c0edaa46162da122d3dd747bc931bb6f8135cd127d747d716c66b5be5a4f469d705ef6ed0f268aec4e36ff2f3952c757586db99382765ef56c19"
)

# List all available backends
backends = service.backends()
print("Available backends:", [getattr(b, 'name', 'Unknown') for b in backends])

# Use confirmed available backend
backend = service.backend("ibm_brisbane")
# Access name attribute safely
backend_name = backend.name if isinstance(getattr(backend, 'name'), str) else backend.name()
print("🔄 Initialized backend:", backend_name)
print("Backend type:", type(backend))
print("Backend name attribute type:", type(getattr(backend, 'name')))