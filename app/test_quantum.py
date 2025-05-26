# test_quantum.py
from quantum_stock_prediction import run_quantum_prediction

if __name__ == "__main__":
    try:
        result = run_quantum_prediction()
        print("Result:", result)
    except Exception as e:
        print("Error:", str(e))