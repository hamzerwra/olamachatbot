# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install necessary dependencies
RUN pip install --upgrade pip
RUN pip install requests flask

# Copy your Python script (e.g., olama_api.py) into the container
COPY olama_api.py /app/

# Expose the port that the Flask app will run on
EXPOSE 5000

# Run the Flask application
CMD ["python", "olama_api.py"]
