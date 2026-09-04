FROM python:3.12-slim

WORKDIR /app

COPY python.py .

# Generate the webpage
RUN python python.py

# Tell Docker the application uses port 8000
EXPOSE 8000

# Keep the container running with a web server
CMD ["python", "-m", "http.server", "8000"]
