Fedora 30 Mate Desktop Post-Install
###################################

:date: 2019-12-24 12:28
:tags: fc30, fedora, mate, postinstall
:category: floss
:slug: mate-desktop
:summary: Fedora 30 Mate Desktop Post-Install
:lang: en

DNF Configuration
=================

dnf.conf
--------

Enable Fastest Mirrors:

.. code-block:: console

   echo 'fastestmirror=true' >> /etc/dnf/dnf.conf

Disable DeltaRPMs for Future Updates:

.. code-block:: console

   echo 'deltarpm=false' >> /etc/dnf/dnf.conf

Enable DNF Package Caching:

.. code-block:: console

   echo 'keepcache=true' >> /etc/dnf/dnf.conf

Disable DNF Makecache Systemd Service and Timer
-----------------------------------------------

To disable the service:

.. code-block:: console

   systemctl disable dnf-makecache.service

To disable the timer:

.. code-block:: console

   systemctl disable dnf-makecache.timer

Regenerate the Cache and Install Available Updates
--------------------------------------------------

As a normal, non-root user:

.. code-block:: console

   dnf clean all

.. code-block:: console

   dnf makecache

For root:

.. code-block:: console

   su -c 'dnf clean all'

.. code-block:: console

   su -c 'dnf makecache'

Reboot:

.. code-block:: console

   reboot

Check for Available Upgrades
============================

Enter your root password:

.. code-block:: console

   su -c 'dnf --refresh check-upgrade'

If upgrades are available, apply them:

.. code-block:: console

   su -c 'dnf upgrade'

Reboot:

.. code-block:: console

   reboot

Mate Desktop Tips and Tricks
============================

Enable Window Compositing:

.. code-block:: console

   gsettings set org.mate.Marco.general compositing-manager true

Enable New Window Centering:

.. code-block:: console

   gsettings set org.mate.Marco.general center-new-windows true

Enable Window Snapping:

.. code-block:: console

   gsettings set org.mate.Marco.general allow-tiling true

Hide All Desktop Icons:

.. code-block:: console

   gsettings set org.mate.background show-desktop-icons false

Change Window Decoration Button Order:

.. code-block:: console

   gsettings set org.mate.Marco.general button-layout 'close,maximize,minimize:menu'

Disable Automount-Open:

.. code-block:: console

   gsettings set org.mate.media-handling automount-open false

Disable Automounting:

.. code-block:: console

   gsettings set org.mate.media-handling automount false

Set Default Caja Preferences for Sorting Order:

.. code-block:: console

   gsettings set org.mate.caja.preferences default-sort-order type

Create Working Directories
==========================

.. code-block:: console

   mkdir ~/git_repos

.. code-block:: console

   mkdir ~/projects

Remove Unneeded Software
========================

.. code-block:: console

   su -c 'dnf -y remove xfburn'

.. code-block:: console

   su -c 'dnf -y remove exaile'

.. code-block:: console

   su -c 'dnf -y remove parole'

.. code-block:: console

   su -c 'dnf -y remove hexchat'

.. code-block:: console

   su -c 'dnf -y remove dnfdragora'

.. code-block:: console

   su -c 'dnf -y remove filezilla'

Software Repositories
=====================

Enable software repositories.

RPMFusion
---------

.. code-block:: console

   su -c 'dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm'

Fedora Workstation Repositories
-------------------------------

.. code-block:: console

   su -c 'dnf install fedora-workstation-repositories'

Fedora Rawhide's Repositories
-----------------------------

.. code-block:: console

   su -c 'dnf install fedora-repos-rawhide'

COPR
----

Copr is an easy-to-use automatic build system providing a package repository as
its output.

`neteler/remarkable`
~~~~~~~~~~~~~~~~~~~~

Remarkable is a free, fully-featured Markdown editor.

.. code-block:: console

   su -c 'dnf -y copr enable neteler/remarkable'

`philfry/gajim`
~~~~~~~~~~~~~~~

Gajim is a Jabber client written in PyGTK. It provides support for the OMEMO
encryption method. This repo includes tools and dependencies not available in
the official Fedora repo.

.. code-block:: console

   su -c 'dnf -y copr enable philfry/gajim'

`dani/qgis`
~~~~~~~~~~~

QGIS is a user-friendly, open-source Geographic Information System.

.. code-block:: console

   su -c 'dnf -y copr enable dani/qgis'

`@dotnet-sig/dotnet`
~~~~~~~~~~~~~~~~~~~~~

This provides the .NET CLI tools and runtime for Fedora.

.. code-block:: console

   su -c 'dnf copr enable @dotnet-sig/dotnet'

VSCodium
--------

Import the GPG key:

.. code-block:: console

   su -c 'rpm --import https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg'

Now create the `vscodium.repo` file:

.. code-block:: console

   su -c "tee -a /etc/yum.repos.d/vscodium.repo << 'EOF'
   [gitlab.com_paulcarroty_vscodium_repo]
   name=gitlab.com_paulcarroty_vscodium_repo
   baseurl=https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/repos/rpms/
   enabled=1
   gpgcheck=1
   repo_gpgcheck=1
   gpgkey=https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg
   EOF
   "
