Installing Cisco Packet Tracer on Fedora 44 Workstation Using Distrobox
#######################################################################

:date: 2026-11-01 19:19
:tags: cisco, distrobox, fc44, fedora, linux, packet-tracer, podman, ubuntu
:category: floss
:slug: cisco-packet-tracer-fedora-44
:summary: A complete step-by-step guide to installing Cisco Packet Tracer 
          9.0.1 on Fedora 44 Workstation using an Ubuntu 24.04 Distrobox 
          container, including fixing FUSE, XCB, and Qt library dependencies.
:lang: en

Cisco Packet Tracer is an essential tool for CCNA students and network 
engineers. However, Cisco officially distributes Packet Tracer as a .deb 
package targeting Ubuntu Linux, making native installation on RPM-based 
distributions like Fedora 44 Workstation tricky.

Rather than dirtying your host Fedora system with converted RPMs or 
extracted binaries, the cleanest solution is to isolate Cisco Packet 
Tracer inside an Ubuntu 24.04 Noble Numbat container via Distrobox.

This guide covers all prerequisite packages, container setup, dependency 
fixes, FUSE symlinks, and desktop integration for Fedora 44 Workstation 
Edition.

----

Host Prerequisites (Fedora 44 Workstation)
==========================================

Before creating the container, ensure your host system has Distrobox, 
Podman, and the legacy FUSE kernel tools installed.

Open a terminal on your Fedora host (taylor) and install the host 
prerequisites:

.. code-block:: bash

   sudo dnf install -y distrobox podman fuse

* **podman / distrobox**: Provides the container runtime and seamless host 
  integration.
* **fuse**: Enables host-level FUSE mounting capabilities required by 
  AppImage binaries inside containers.

----

Step 1: Create and Enter the Ubuntu Container
=============================================

Create an Ubuntu 24.04 container named ``ubuntu-pt``:

.. code-block:: bash

   distrobox-create --name ubuntu-pt --image ubuntu:24.04

Once creation completes, enter the container shell:

.. code-block:: bash

   distrobox-enter -n ubuntu-pt

----

Step 2: Install Container Base Dependencies
===========================================

Inside your ``ubuntu-pt`` container shell, update package lists and 
install the core desktop and FUSE dependencies required by Ubuntu 24.04:

.. code-block:: bash

   sudo apt update
   sudo apt install -y fuse3 libglib2.0-bin desktop-file-utils shared-mime-info

Setting Up the FUSE Symlink
---------------------------

Cisco Packet Tracer's internal AppImage loader specifically calls 
``fusermount``, whereas Ubuntu 24.04 relies on ``fusermount3``. Create a 
symbolic link inside the container to prevent AppImage mounting failures:

.. code-block:: bash

   sudo ln -sf /usr/bin/fusermount3 /usr/bin/fusermount

----

Step 3: Install Cisco Packet Tracer .deb Package
================================================

Download the ``CiscoPacketTracer_901_Ubuntu_64bit.deb`` file into your host 
``~/Downloads`` directory (which is automatically mounted inside Distrobox).

Inside the container, navigate to your downloads folder and install the 
package:

.. code-block:: bash

   sudo apt install ./Downloads/CiscoPacketTracer_901_Ubuntu_64bit.deb

.. note::

   You may see a notice stating: ``N: Download is performed unsandboxed as root...``. 
   This is safe to ignore; it simply indicates apt fell back to root 
   privileges to read files from your home directory.

During installation, accept the End User License Agreement (EULA). When 
prompted:

.. code-block:: text

   Would you like to run multi-user when application starts?

Select **No** unless you are setting up a multi-tenant shared computer lab.

----

Step 4: Resolve Runtime GUI and Library Dependencies
====================================================

Cisco Packet Tracer depends on several dynamic libraries that are omitted 
from minimal container base images. Run the following command inside the 
container to install all missing audio, graphics, security, and XCB display 
dependencies:

.. code-block:: bash

   sudo apt install -y \
       libopengl0 \
       libgl1 \
       libnss3 \
       libnspr4 \
       libxss1 \
       libasound2t64 \
       libpulse0 \
       libxcb-xinerama0 \
       libxcb-cursor0 \
       libxkbcommon-x11-0 \
       libxcb-icccm4 \
       libxcb-image0 \
       libxcb-keysyms1 \
       libxcb-randr0 \
       libxcb-render-util0 \
       libxcb-shape0 \
       libxcb-xfixes0

Summary of key dependencies:

* **libopengl0 & libgl1**: Provides OpenGL rendering for the device canvas.
* **libnss3 & libnspr4**: Enables internal web view components.
* **libasound2t64 & libpulse0**: Handles PulseAudio client audio routing.
* **libxcb-***: Provides X11/XCB platform plugins for Qt application 
  window rendering.

Now exit the container shell:

.. code-block:: bash

   exit

----

Step 5: Desktop Integration on Fedora Host
==========================================

To launch Cisco Packet Tracer directly from your Fedora GNOME Application 
menu, create a custom ``.desktop`` launcher entry on your host system.

Open your text editor on the Fedora host:

.. code-block:: bash

   vi ~/.local/share/applications/packettracer.desktop

Paste the following configuration:

.. code-block:: ini

   [Desktop Entry]
   Name=Cisco Packet Tracer
   Comment=Networking Simulation Tool
   Exec=distrobox-enter -n ubuntu-pt -- packettracer
   Terminal=false
   Type=Application
   Categories=Education;Network;
   StartupNotify=true

Save the file and update the desktop launcher database:

.. code-block:: bash

   update-desktop-database ~/.local/share/applications/

Testing the Installation
------------------------

You can now launch Cisco Packet Tracer directly from your terminal:

.. code-block:: bash

   distrobox-enter -n ubuntu-pt -- packettracer

Or simply search for Cisco Packet Tracer in your GNOME Super/Activities 
launcher!
