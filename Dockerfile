# Use a minimal Python base image
FROM python:slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
# git is needed to clone your repository
# build-essential might be needed if your Python packages have C extensions (remove if not needed)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy your requirements.txt file into the container
# This is done early to leverage Docker's layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your blog source code into the container
# This should be the last step so that changes to your code don't invalidate previous layers
COPY . .

# (Optional) Define a default command to run when the container starts
# Replace 'python your_generator.py' with the actual command to run your generator
#CMD ["python", "your_generator.py", "build"]
