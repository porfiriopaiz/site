Fedora 26 Custom Operating System post install
##############################################

:date: 2017-8-31 16:26
:tags: dnf, fc26, fedora, postinstall
:category: floss
:slug: fedora-26-custom-operating-system-post-install
:summary:
:lang: en

On the last post I explained how make a Minimal install of Fedora 25, months
has passed by since the last post and Fedora 26 was released, following the
same steps I installed it on my laptop and next I will document my postinstall.

Given this is a minimal install, the set of packages installed does not
provides support for Wireless Network Cards. It is true that during the
installation process Anaconda provides such support, but once you have
installed the minimal set of packages, these does not provides the required
drivers, for this matter I must get my laptop connected to a Wired Network.

``dnf`` configuration
=====================

After checking the Wired Network, first I did was to edit dnf's configuration
file and add the next lines to it:

.. code-block:: console

   echo 'fastestmirror=true' >> /etc/dnf/dnf.conf

   echo 'deltarpm=false' >> /etc/dnf/dnf.conf

   echo 'keepcache=true' >> /etc/dnf/dnf.conf

This way I make sure ``dnf`` will always use the more efficient mirror; will
not use `*.drpm's` for upgrades, instead it will always download `*.rpm's`; and
will keep any package it downloads in its cache.

Now let's reboot:

.. code-block:: console

   reboot

Disablle dnf-makecache.service and dnf-makecache.timer
======================================================

``dnf`` has this service and timer that annoys me, both makes sure of keeping
the package metadata cache up to date with a certain frequence, this is
something I like to do when I want and when I need it, not at ``dnf`` please,
so this behaviour is fixed with the next command:

.. code-block:: console

   su -c 'systemctl disable dnf-makecache.service'

   su -c 'systemctl disable dnf-makecache.timer'

Let's reboot again:

.. code-block:: console

   reboot

Rebuilding packages metadata cache's
====================================

Once ``dnf`` configuration file is customized, service and timer are disabled,
I clean the old cache and rebuild it. This time the commands are run as normal
user, Fedora keeps two differents cache: one for the normal user and other for
the root user:

This will rebuild packages metadata cache for my normal user:

.. code-block:: console

   dnf clean all

   dnf makecache

This will rebuild packages metadata cache for the root user:

.. code-block:: console

   su -c 'dnf clean all'

   su -c 'dnf makecache'

Available Upgrades
==================

During the installation it is possible to mark a checkbox for the option to
download and install the packages with the most recent version, to verify if
there aren't any upgrades:

.. code-block:: console

   su -c 'dnf --refresh check-upgrade'

To download and apply the upgrades if availables:

.. code-block:: console

   su -c 'dnf upgrade'

After the upgrade let's reboot to make use of latest version of any package if
upgraded.

.. code-block:: console

   reboot

Workstation Product Environment Installation
============================================

On my laptop I use GNOME Shell as desktop environment, to install it I make use
of a package group that provides all the required packages to make of this
Fedora Custom Operating System install a Fedora Workstation:

.. code-block:: console

   su -c 'dnf group install workstation-product-environment'

Graphical Boot Mode
===================

After downloading and installing all the packages, We must change the default
`init` mode from ``multi-user.target`` to ``graphical.target``, otherwise, when
We reboot our system will not start in graphical mode.

Also We must enable the service for the graphical login manager, if no, despite
enabling the graphical mode our login will still a text based prompt:

.. code-block:: console

   su -c 'systemctl set-default graphical.target'

   su -c 'systemctl enable gdm.service'

   reboot

If nothing goes wrong, you might be running Fedora 26 Workstation with GNONE
Shell.

Fixing Nautilus Behaviour
=========================

Before opening any other application, I like to fix how Nautilus sorts files, I
like to have them sorted by type or file extension:

.. code-block:: console

   gsettings set org.gnome.nautilus.preferences default-sort-order type

This way when opening Nautilus it will show the files sorted by extension.

Repositories
============

Enabling RPMFusion:
-------------------

.. code-block:: console

   su -c 'dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm'

Refresh the cache, this will download the RPMFusion packages metadata:

.. code-block:: console

   su -c 'dnf check-upgrade'

Enabling Google Chrome's repository:
------------------------------------

I used to enable Google Chrome repository as explained on this post:

`https://www.if-not-true-then-false.com/2010/install-google-chrome-with-yum-on-fedora-red-hat-rhel/ <https://www.if-not-true-then-false.com/2010/install-google-chrome-with-yum-on-fedora-red-hat-rhel/>`_.

But Mayorga presented me a more simple method, basically you just have to
download Google Chrome ``rpm`` package, install it from the command line
indicating the path to the ``rpm`` package and this by itself will add the
`*.repo` file to the path ``/etc/yum.repos.d/``.

.. code-block:: console

   cd ~/Downloads

   wget -N -t 0 -c https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm

   su -c 'dnf install google-chrome-stable_current_x86_64.rpm'

   su -c 'dnf check-update'

Disabling Tracker
=================

Before copying back any file from my back up's, hay must disable the annoying
``tracker`` and all his friends:

.. code-block:: console

   su -c 'dnf install tracker-preferences'

   mkdir ~/.config/autostart

   cp /etc/xdg/autostart/tracker* ~/.config/autostart

   cd ~/.config/autostart

   sed -i 's/X-GNOME-Autostart-enabled=true/X-GNOME-Autostart-enabled=false/' tracker*

Let's check ``tracker`` status:

.. code-block:: console

   tracker status

Then we make a ``hard reset``:

.. code-block:: console

   tracker reset --hard

Disabling GNOME Software and PackageKit download-updates
========================================================

GNOME Software downloads metadata and upgrades for the system in background, to
disable it We execute the next commands:

.. code-block:: console

   gsettings set org.gnome.software download-updates false

   su -c 'systemctl mask packagekit.service'

This should stop the autodownload upgrades and the PackageKit service.

Libraries and Development Tools
===============================

Now install the package groups that provides the required software and
libraries for compiling other software from source code, as well as making of
``vim`` and `IDE`, on another post I will explain how to do so:

.. code-block:: console

   su -c 'dnf -y groups install c-development'

   su -c 'dnf -y groups install development-libs'

   su -c 'dnf -y groups install development-tools'

   su -c 'dnf -y groups install fedora-packager'

   su -c 'dnf -y groups install rpm-development-tools'

   su -c 'dnf install automake gcc gcc-c++ kernel-devel cmake'

   su -c 'dnf install python-devel python3-devel'

   su -c 'dnf install monodevelop'

   su -c 'dnf install golang'

   su -c 'dnf install nodejs'

   su -c 'dnf install rust'

   su -c 'dnf install cargo'

   su -c 'dnf install python3-virtualenv'

   su -c 'dnf install python3-pip'

And finally the spellcheckers:

.. code-block:: console

   su -c 'dnf install hunspell'

   su -c 'dnf install hunspell-en'

   su -c 'dnf install hunspell-es'

   su -c 'dnf install aspell'

   su -c 'dnf install aspell-es'

   su -c 'dnf install aspell-en'

   su -c 'dnf install autocorr-es'

   su -c 'dnf install autocorr-en'

On the next post I will make shorts reviews on the other tools I use on Fedora.
