#main.py to run the FastAPI server and serve the quantum stock prediction API
# This file is part of Quantum Stock Prediction.
# output: A FastAPI server that serves two endpoints for stock prediction using quantum computing.
# Expected input: A trained quantum model and stock data in a JSON format.
# author: Ranjan Kumar  
# date: 2025-05-21
from fastapi import FastAPI
from typing import Dict, Any
from quantum_stock_prediction import predict_stock, run_quantum_prediction

app = FastAPI()

@app.get("/test")
def test():
    return {"message": "Test endpoint working"}

@app.get("/predict_stock", response_model=Dict[str, Any])
def predict():
    return predict_stock()

@app.get("/predict_quantum", response_model=Dict[str, Any])
def predict_quantum():
    try:
        return run_quantum_prediction()
    except Exception as e:
        return {"error": str(e)}