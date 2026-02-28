You're absolutely right; I missed some of the critical "start from scratch" and directory navigation steps we covered earlier. I've integrated the full sequence—from cloning the repo to the final "nuclear" cleanup—into this updated version.

# Pelican Static Site Generator (Podman Edition)

These are my notes for setting up a containerized environment for Pelican. By using Podman, the entire Python stack is isolated from the host OS, avoiding version conflicts and ensuring a reproducible build environment.

## Why use this Containerized Guide?

Instead of managing local `virtualenvs` or system-level Python packages, this guide uses a **minimal Podman image**.

* **True Portability**: The same environment works on any machine with Podman installed.
* **Isolation**: No risk of polluting or breaking the system Python.
* **Cleanliness**: All dependencies (Git, Pelican, Markdown) live inside the image.

---

## 1. Initial Setup

### Clone the Repository

Navigate to your git directory and clone your site sources:

```sh
cd ~/git_repos/github.com/porfiriopaiz/
git clone git@github.com:porfiriopaiz/site.git
cd site/

```

### Configuration Files

Ensure your `requirements.txt` and `Dockerfile`  are in the root of the `site/` directory.

**Dockerfile:** 

```dockerfile
FROM python:slim
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends git make && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# No COPY . . is used because we mount the local directory as a volume
CMD ["sleep", "infinity"]

```

---

## 2. Build and Launch

### Build the Image

Tag the image as `pelican`:

```sh
podman build -t pelican .

```

### Run the Container

Launch the container with port forwarding and volume mounting. Note the `:Z` suffix to handle SELinux permissions:

```sh
podman run -d \
  -v $(pwd):/app:Z \
  --name site \
  -p 8000:8000 \
  pelican

```

---

## 3. Pelican Workflow

### Generate the Site

If your image includes `make`, use the standard command:

```sh
podman exec -it site make html

```

Alternatively, use the direct Pelican command:

```sh
podman exec -it site pelican content -s pelicanconf.py

```

### Serve Locally

To preview your site at `http://localhost:8000`, bind to `0.0.0.0`:

```sh
podman exec -it site pelican -l -p 8000 -b 0.0.0.0

```

---

## 4. Maintenance & Reset

### Cleaning the Workspace

If you need to start from a "Clean Slate," run this sequence to remove the container, the image, and local build artifacts:

```sh
# Stop and remove container
podman stop site && podman rm site

# Remove image
podman rmi pelican

# Deep clean system and local artifacts
podman system prune -f
rm -rf output/ cache/ __pycache__/

```

### Deployment (GitHub Pages)

```sh
git checkout master
git subtree split --prefix output -b gh-pages
git push -f origin gh-pages:gh-pages
git branch -D gh-pages

```

---
