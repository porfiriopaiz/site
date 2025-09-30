Podman, a Python Environment, and Pelican
#########################################

:date: 2025-9-15 2:15
:tags: pelican, podman, python
:category: floss
:slug: podman-python-env-pelican
:summary: How to set up a Python environment for Pelican within a
          Podman container
:lang: en

Ever wanted to manage your static blog without cluttering your local
machine with Python environments? **Podman** offers a clean, isolated
way to do just that! This post will guide you through setting up a
minimal Podman image to provide the requirements for an existing
static site generator using **Pelican**.

----

Prepare Your Project Directory
------------------------------

I have been using Pelican to generate the contents of this blog,
starting from .rst files. From the very beginning, I have been using
the Python Virtual Environment module, along with ``git`` and the
pre-included bash shell scripts that Pelican provides when static
content is first generated. I have always been curious about using
Docker to make this portable and easy to reproduce regardless of the
platform I'm using at the moment, whether it's GNU/Linux (Fedora,
Debian, Arch...) or macOS, which I've been using recently.

Having something that would ease this process is beneficial. In this
case, I will not be starting from the stage where you configure the
metadata for the static site generator that will be used for your
project, but rather from cloning the existing Git repository that
contains the previous entries and outputs of this blog.

.. code-block:: bash

   cd ~/git_repos/github.com/porfiriopaiz/

.. code-block:: bash

   git clone git@github.com:porfiriopaiz/site.git

.. code-block:: bash

   cd site/

----

Define Python Dependencies (``requirements.txt``)
-------------------------------------------------

Inside my ``site`` directory, I created a file named
``requirements.txt``. This file lists all the Python packages your
static site generator (Pelican, in this case) needs.

.. code-block:: text

   # site/requirements.txt
   pelican
   markdown
   typogrify
   feedgenerator
   jinja2
   pygments
   docutils
   blinker
   unidecode
   MarkupSafe
   python-dateutil

- ``pelican``: The core static site generator.
- ``markdown``: Essential if you plan to write your content in Markdown
  format.
- ``typogrify``: For optional typographical enhancements.
- The rest are automatically installed dependencies for Pelican.

----

Create Your Dockerfile
----------------------

Next, I created a file named ``Dockerfile`` (no extension) in the root
of the ``my-pelican-blog`` directory. This file instructs Podman on
how to build the image that is going to be used by ``podman`` to
create the *site* container.

.. code-block:: dockerfile

   # Use a minimal Python base image
   FROM python:slim

   # Set the working directory in the container
   WORKDIR /app

   # Install system dependencies
   # git is needed to clone your repository
   # build-essential might be needed if your Python packages have C
   # extensions (remove if not needed)
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
   # This should be the last step so that changes to your code don't
   # invalidate previous layers
   COPY . .

   # (Optional) Define a default command to run when the container starts
   # Replace 'python your_generator.py' with the actual command to run
   # your generator
   #CMD ["python", "your_generator.py", "build"]

----

Build Your Podman Image
-----------------------

With the ``Dockerfile`` and ``requirements.txt`` in place, navigate
your terminal to the ``site`` directory and build your Podman image.
We'll tag it ``site``.

.. code-block:: bash

   podman build -t pelican .

- ``podman build``: The command to build an image.
- ``-t pelican``: Tags the resulting image with the name ``pelican``.
- ``.``: Specifies that the build context (where Podman looks for
  ``Dockerfile`` and other files) is the current directory.

You can verify your image exists by running ``podman images``.

----

Run Your Podman Container (with Port Forwarding)
------------------------------------------------

Now, let's run the container. To make your Pelican development server
accessible from your host machine (e.g., in your browser at
`http://localhost:8000/`), you **must forward the port**.

.. code-block:: bash

   podman run -d -v $(pwd):/app --name site -p 8000:8000 pelican:latest sleep infinity

Let's break down this command:

- ``podman run``: Starts a new container.
- ``-d``: Runs the container in **detached mode** (in the background),
  so your terminal prompt returns immediately.
- ``-v $(pwd):/app``: This is a **volume mount**. It mounts your
  current host directory (``$(pwd)``) to the ``/app`` directory inside
  the container. This means any changes you make to your blog files on
  your host are immediately reflected inside the container.
- ``--name site``: Assigns the name ``site`` to your running
  container, making it easy to reference later.
- ``-p 8000:8000``: This is crucial for **port forwarding**. It maps
  port ``8000`` on your **host machine** to port ``8000`` inside the
  **container**. Your Pelican server will run on 8000 inside the
  container, and this mapping makes it accessible on your host's 8000.
- ``pelican:latest``: Specifies that you're creating the container from the
  ``pelican:latest`` image you just built.
- ``sleep infinity``: This command runs indefinitely inside the
  container, keeping it alive so you can interact with it later.

You can check if the container is running with ``podman ps``.

----

Generate Your Site and Serve It
-------------------------------

With the container running and the port mapped, you can now execute
commands inside it.

Initialize Your Pelican Project (First Time Only)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If this is your first time, you'll want to use ``pelican-quickstart``
to set up the basic project structure:

.. code-block:: bash

   podman exec -it site bash

Once inside the container shell:

.. code-block:: bash

   cd /app

.. code-block:: bash

   pelican-quickstart

Follow the prompts. When it asks for the project path, the default
(current working directory) is usually fine, as ``/app`` is your
mounted host directory. Your project will consist of a hierarchy
including ``content``, ``output``, ``pelicanconf.py``, and
``publishconf.py``.

After ``pelican-quickstart`` finishes, type ``exit`` or ``Ctrl+D`` to
leave the container's shell.

Start the Pelican Development Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After adding some lines with reStructuredText markup within a .rst
file, you can use it as the source to build a blog post that will be
exported under the ``content`` directory as an .html file.

To build this .html file from the source .rst file, you will use the
following command to build your site and then serve it:

.. code-block:: bash

   podman exec -it site make html

Then:

.. code-block:: bash

   podman exec -it site make serve

This command runs ``make serve`` inside your ``site`` container. This
process will typically occupy your terminal, displaying logs from the
server.

----

View Your Blog! 🌐
------------------

Open your web browser and navigate to:

`http://localhost:8000/`

You should now see your Pelican blog! Any changes you make to your
content files on your host machine will be automatically picked up by
Pelican's development server (if configured to reload) and reflected in
your browser.

----

Stopping and Restarting Your Container
--------------------------------------

When you're done developing:

Stop the Server
^^^^^^^^^^^^^^^

Go back to the terminal running ``make serve`` (where your prompt is
not visible) and press ``Ctrl+C``. This will stop the ``make serve``
process. Your prompt will return.

Stop the Container
^^^^^^^^^^^^^^^^^^

To stop the Podman container itself:

.. code-block:: bash

   podman stop site

Restart the Container
^^^^^^^^^^^^^^^^^^^^^

To run it again later without recreating it:

.. code-block:: bash

   podman start site

Then, re-execute ``podman exec -it site make serve`` to restart your
development server.

----

Cleaning Up (Optional)
----------------------

If you're completely done and want to remove the container and image:

Remove the Container
^^^^^^^^^^^^^^^^^^^^

(Ensure it's stopped first)

.. code-block:: bash

   podman rm site

Remove the Image
^^^^^^^^^^^^^^^^

(Ensure no containers are using it)

.. code-block:: bash

   podman rmi pelican

By following these steps, you've built a portable, isolated
environment for your static site generator, keeping your local machine
clean and tidy!
