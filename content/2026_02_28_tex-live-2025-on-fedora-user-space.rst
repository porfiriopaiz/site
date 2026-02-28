Installing TeX Live 2025 on Fedora: A Minimalist User-Space Guide
#################################################################

:date: 2026-02-28 04:40
:tags: fedora, latex, linux, texlive
:category: floss
:slug: texlive-2025-fedora-user-space
:summary: A comprehensive guide to installing a full, upstream TeX Live
          distribution within a user's home directory on Fedora Linux.
:lang: en

This guide consolidates the steps required to establish a professional-grade
LaTeX environment into a single, clean workflow. Following this chronological
order ensures that directories exist, dependencies are met, and the
environment is correctly configured before the software attempts to utilize them.

By installing TeX Live in user-space (within ``~/.local/opt``), we adhere to a
minimalist philosophy. This approach avoids cluttering the system root,
removes the need for ``sudo`` during package management via ``tlmgr``, and
ensures you are using the most recent upstream binaries rather than
potentially outdated distribution packages.

----

Pre-Installation: System Dependencies
=====================================

Fedora's "minimal" Perl and X11 profiles often lack specific libraries
required by the TeX Live installer and its graphical management tools.
While we aim for a lean system, these Perl modules are essential for the
installer's checksum verification and the ``tlmgr`` interface.

Install these requirements using ``dnf``:

.. code-block:: bash

   sudo dnf install perl-File-Find perl-File-Copy perl-Digest-MD5 perl-Tk perl-Term-ANSIColor xdotool

----

Create the Directory Structure
==============================

We will create a "user-space system" directory. Utilizing ``~/.local/opt``
keeps your home directory organized while mimicking the Linux Filesystem
Hierarchy Standard (FHS).

.. code-block:: bash

   mkdir -p ~/.local/bin

.. code-block:: bash

   mkdir -p ~/.local/opt/texlive

----

Download and Launch the Installer
=================================

To avoid "checksum mismatch" errors common with unstable local mirrors, we
will point the installer directly to the Comprehensive TeX Archive Network
(CTAN) global repository.

.. code-block:: bash

   cd ~/Downloads

.. code-block:: bash

   wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz

.. code-block:: bash

   tar -xzf install-tl-unx.tar.gz

.. code-block:: bash

   cd install-tl-*

Launch the installer using a reliable global mirror:

.. code-block:: bash
 
   ./install-tl -repository http://mirror.ctan.org/systems/texlive/tlnet/

----

Installer Configuration (Text Menu)
===================================

Once the command-line interface menu appears, you must modify specific
installation paths to point to your local directories:

1. **Directories (D)**: Change ``TEXDIR`` to:
   ``/home/porfirio/.local/opt/texlive/2025``

2. **Options (O)**:
   * Toggle **Paper Size** to ``letter``.
   * Toggle **Create symlinks** (``L``) to ``[X]``.
   * **Binaries**: ``/home/porfirio/.local/bin``
   * **Manpages**: ``/home/porfirio/.local/share/man``
   * **Info**: ``/home/porfirio/.local/share/info``

3. **Install (I)**: Start the process.

.. note::
   The full installation can take approximately 3 hours depending on your
   connection. It is highly recommended to run this inside a ``tmux``
   session to prevent the installation from terminating if your terminal
   session disconnects.

----

Post-Installation: Environment Setup
====================================

Fedora needs to be instructed where to find these new binaries. We will
create a modular profile script in ``~/.bashrc.d/`` to keep our
``~/.bashrc`` clean.

Create the configuration file:

.. code-block:: bash

   vi ~/.bashrc.d/texlive.sh

**Paste the following content into the file:**

.. code-block:: bash

   # TeX Live 2025 Path Configuration
   TEX_BIN_PATH="/home/porfirio/.local/opt/texlive/2025/bin/x86_64-linux"

   if [ -d "$TEX_BIN_PATH" ]; then
       # Prioritize TeX binaries and your local bin folder
       export PATH="$TEX_BIN_PATH:/home/porfirio/.local/bin:$PATH"
       export INFOPATH="/home/porfirio/.local/opt/texlive/2025/texmf-dist/doc/info:$INFOPATH"
       export MANPATH="/home/porfirio/.local/opt/texlive/2025/texmf-dist/doc/man:$MANPATH"
   fi

**Apply the changes to your current session:**

.. code-block:: bash

   source ~/.bashrc

----

Finalizing the Formats
======================

With the paths set and Perl dependencies satisfied, manually execute the
tasks that occasionally fail during the installer's finalization stage
due to environment restrictions:

.. code-block:: bash

   # Set default paper size
   tlmgr paper letter

.. code-block:: bash

   # Build the format files (Engines)
   fmtutil-sys --all

----

Verification and Troubleshooting
================================

To ensure your system is ready for document production, perform a "smoke test"
by checking the binary location and compiling a dummy document.

Check the Binary Path
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   which pdflatex

This should return a path pointing to your ``~/.local/bin/`` or
``~/.local/opt/`` folder rather than ``/usr/bin/``.

Compile a Test Document
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   echo "\documentclass{article}\begin{document}LaTeX 2025 is Live on Fedora!\end{document}" > test.tex

.. code-block:: bash

   pdflatex test.tex

----

Summary of Locations
====================

For future maintenance on your system, keep these paths in mind:

* **The System Root**: ``~/.local/opt/texlive/2025/``
* **The Binaries/Symlinks**: ``~/.local/bin/``
* **The Configuration**: ``~/.bashrc.d/texlive.sh``
* **The Logs**: ``~/.local/opt/texlive/2025/texmf-var/web2c/fmtutil.log``

You now have a professional-grade, upstream LaTeX installation that is
completely independent of Fedora's system packages, making it easy to
back up or migrate to a new machine in the future.
