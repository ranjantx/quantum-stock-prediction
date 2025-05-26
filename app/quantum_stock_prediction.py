#quantum_stock_prediction.py with run_quantum_prediction() and predict_stock()
import os
from qiskit.circuit.library import ZZFeatureMap
from qiskit_machine_learning.kernels import QuantumKernel
from qiskit_machine_learning.algorithms import QSVC
from qiskit.utils import algorithm_globals
from qiskit import QuantumCircuit, ClassicalRegister, BasicAer
import numpy as np
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from fastapi import HTTPException

def run_quantum_prediction():
    print("🔄 Starting IBM Quantum prediction...")
    # Mocking the quantum result to bypass the SamplerV2 error
    print("⚠️ Mocking quantum result for deployment testing...")
    mocked_result = {'00': 0.25, '01': 0.25, '10': 0.25, '11': 0.25}
    print("✅ Mocked counts:", mocked_result)
    return {"counts": mocked_result}

def predict_stock():
    algorithm_globals.random_seed = 12345
    X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_train = np.array([0, 1, 1, 0])
    feature_map = ZZFeatureMap(feature_dimension=2, reps=1)
    quantum_kernel = QuantumKernel(feature_map=feature_map, quantum_instance=BasicAer.get_backend("qasm_simulator"))
    model = QSVC(quantum_kernel=quantum_kernel)
    model.fit(X_train, y_train)
    test_sample = np.array([[0.5, 0.5]])
    prediction = model.predict(test_sample)
    return {"input": test_sample.tolist(), "predicted_class": int(prediction[0])}