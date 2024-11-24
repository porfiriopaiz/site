Fedora 26 Custom Operating System Post-Install
###############################################

:date: 2017-8-31 16:26
:tags: dnf, fc26, fedora, postinstall
:category: floss
:slug: fedora-26-custom-operating-system-post-install
:summary:
:lang: en

In the last post, I explained how to make a minimal installation of Fedora 25.
Months have passed since then, and Fedora 26 has been released. Following the
same steps, I installed it on my laptop and will now document my
post-installation process.

Since this is a minimal installation, the set of installed packages does not
provide support for wireless network cards. Although Anaconda provides such
support during the installation process, the minimal package set lacks the
required drivers. To address this, I connected my laptop to a wired network.

``dnf`` Configuration
=====================

After connecting to a wired network, the first thing I did was edit ``dnf``'s
configuration file and add the following lines:

.. code-block:: console

   echo 'fastestmirror=true' >> /etc/dnf/dnf.conf
   echo 'deltarpm=false' >> /etc/dnf/dnf.conf
   echo 'keepcache=true' >> /etc/dnf/dnf.conf

This ensures that ``dnf`` always uses the fastest mirror, avoids using `*.drpm`
files for upgrades (downloading `*.rpm` files instead), and retains any
downloaded packages in its cache.

Now, let's reboot:

.. code-block:: console

   reboot

Disable ``dnf-makecache.service`` and ``dnf-makecache.timer``
============================================================

``dnf`` has a service and timer that keep the package metadata cache updated
periodically. This behavior annoys me, as I prefer to update the cache when I
want and need to. To disable these, I ran the following commands:

.. code-block:: console

   su -c 'systemctl disable dnf-makecache.service'
   su -c 'systemctl disable dnf-makecache.timer'

Let's reboot again:

.. code-block:: console

   reboot

Rebuilding Package Metadata Cache
=================================

After customizing the ``dnf`` configuration file and disabling the service and
timer, I cleaned the old cache and rebuilt it. Fedora maintains two separate
caches: one for the normal user and another for the root user.

To rebuild the cache for my normal user:

.. code-block:: console

   dnf clean all
   dnf makecache

To rebuild the cache for the root user:

.. code-block:: console

   su -c 'dnf clean all'
   su -c 'dnf makecache'

Available Upgrades
==================

During installation, there is an option to download and install the latest
versions of packages. To check for any available upgrades:

.. code-block:: console

   su -c 'dnf --refresh check-upgrade'

To download and apply the upgrades, if available:

.. code-block:: console

   su -c 'dnf upgrade'

After upgrading, reboot to utilize the latest versions of any upgraded
packages:

.. code-block:: console

   reboot

Workstation Product Environment Installation
============================================

On my laptop, I use GNOME Shell as my desktop environment. To install it, I
used a package group that provides all the necessary packages to transform this
minimal installation into a Fedora Workstation:

.. code-block:: console

   su -c 'dnf group install workstation-product-environment'

Graphical Boot Mode
===================

After installing the required packages, we must change the default `init` mode
from ``multi-user.target`` to ``graphical.target``. Otherwise, the system will
not boot into graphical mode. Additionally, we need to enable the graphical
login manager service. Without this, the login will remain a text-based prompt:

.. code-block:: console

   su -c 'systemctl set-default graphical.target'
   su -c 'systemctl enable gdm.service'
   reboot

If everything works correctly, Fedora 26 Workstation with GNOME Shell should
now be running.

Fixing Nautilus Behavior
=========================

Before opening any other application, I like to adjust how Nautilus sorts
files. I prefer sorting by type or file extension:

.. code-block:: console

   gsettings set org.gnome.nautilus.preferences default-sort-order type

This ensures files are displayed sorted by extension when opening Nautilus.

Repositories
============

Enabling RPMFusion:
-------------------

.. code-block:: console

   su -c 'dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm'

Refresh the cache to download the RPMFusion package metadata:

.. code-block:: console

   su -c 'dnf check-upgrade'

Enabling Google Chrome's Repository:
------------------------------------

I used to enable the Google Chrome repository as explained in this post:

`https://www.if-not-true-then-false.com/2010/install-google-chrome-with-yum-on-fedora-red-hat-rhel/ <https://www.if-not-true-then-false.com/2010/install-google-chrome-with-yum-on-fedora-red-hat-rhel/>`_.

However, a simpler method was introduced to me by Mayorga. Simply download the
Google Chrome ``rpm`` package, install it via the command line, and it will
automatically add the `*.repo` file to `/etc/yum.repos.d/`.

.. code-block:: console

   cd ~/Downloads
   wget -N -t 0 -c https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
   su -c 'dnf install google-chrome-stable_current_x86_64.rpm'
   su -c 'dnf check-update'

Disabling Tracker
=================

Before copying files from my backups, I disable the annoying ``tracker``
service:

.. code-block:: console

   su -c 'dnf install tracker-preferences'
   mkdir ~/.config/autostart
   cp /etc/xdg/autostart/tracker* ~/.config/autostart
   cd ~/.config/autostart
   sed -i 's/X-GNOME-Autostart-enabled=true/X-GNOME-Autostart-enabled=false/' tracker*

To check ``tracker`` status:

.. code-block:: console

   tracker status

To perform a ``hard reset``:

.. code-block:: console

   tracker reset --hard

Disabling GNOME Software and PackageKit Auto-Updates
====================================================

GNOME Software downloads metadata and updates in the background. To disable
this behavior:

.. code-block:: console

   gsettings set org.gnome.software download-updates false
   su -c 'systemctl mask packagekit.service'

Libraries and Development Tools
===============================

Finally, I installed package groups and tools for development:

.. code-block:: console

   su -c 'dnf -y group install c-development development-libs development-tools fedora-packager rpm-development-tools'

.. code-block:: console

   su -c 'dnf install automake gcc gcc-c++ kernel-devel cmake python-devel python3-devel monodevelop golang nodejs rust cargo python3-virtualenv python3-pip'

To install spell checkers:

.. code-block:: console

   su -c 'dnf install hunspell hunspell-en hunspell-es aspell aspell-es aspell-en autocorr-es autocorr-en'

In the next post, I will review additional tools I use on Fedora.
