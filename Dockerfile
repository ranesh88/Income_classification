# Use official Python image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy only necessary files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app files
COPY app.py .
COPY rf_classifier.joblib .
COPY full_pipeline.joblib .
COPY templates/ ./templates/

# Expose Flask's default port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
