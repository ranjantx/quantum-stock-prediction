# Use a slim Python 3.11 image
FROM python:3.11-slim

ENV IBM_QUANTUM_TOKEN="9ad7e3042518c0edaa46162da122d3dd747bc931bb6f8135cd127d747d716c66b5be5a4f469d705ef6ed0f268aec4e36ff2f3952c757586db99382765ef56c19"

# Set the working directory inside the container
WORKDIR /app

#Install system dependencies
# Copy only requirements to cache dependencies early
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the full application code
COPY ./app .

# Expose FastAPI default port
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
