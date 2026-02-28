# Use a minimal Python base image 
FROM python:slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
# Removed build-essential to keep the image as small as possible
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git && \
    rm -rf /var/lib/apt/lists/*

# Copy your requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies [cite: 2]
RUN pip install --no-cache-dir -r requirements.txt

# We omit the COPY command for the source code because you are 
# using 'podman run -v' to mount your local directory to /app [cite: 3]

# (Optional) Define a default command to run when the container starts
CMD ["sleep", "infinity"]
