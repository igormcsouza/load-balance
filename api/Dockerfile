# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /api

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy your API Python file into the container
COPY api.py .

# Expose the port on which your FastAPI application will run
EXPOSE 8000

# Command to run your FastAPI application
CMD ["uvicorn", "api:api", "--host", "0.0.0.0", "--port", "8000"]
