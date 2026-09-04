
# Use Python official image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy Python file into container
COPY python.py .

# Run the Python program
CMD ["python", "python.py"]
