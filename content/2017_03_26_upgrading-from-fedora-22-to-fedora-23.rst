Upgrading from Fedora 22 to Fedora 23
#####################################

:date: 2017-3-26 16:46
:tags: dnf, eol, fc22, fc23, fedora, system-upgrade
:category: floss
:slug: upgrading-from-fedora-22-to-fedora-23
:summary:
:lang: en

From May 26th in 2015 to November 22th in 2016 I was using Fedora 22 on my
Lenovo ThinkPad T440p, which is equivalent to a year and a half running F22. On
July 19th of 2016 F22 entered `EOL
<https://fedoraproject.org/wiki/End_of_life>`_ status, which means that you
will not receive any further security or maintenance updates, so upgrading to a
newer stable version was recommended.

In this post I will explain how to update to Fedora 23 using the dnf package
manager.

.. TEASER_END

After using Fedora 22 for a year and a half, the packages cache had taken
approximately 10GB of space on my hard drive:

.. image:: {filename}/images/fc22_to_fc23/screenshot_from_2016-11-22_16-05-06.png
   :align: center

To tell dnf to preserve the packages downloaded in the cache it is required to
add the following line to the dnf configuration file ``/etc/dnf/dnf.conf``:

.. code-block:: console

    su -c "echo 'keepcache = true' >> /etc/dnf/dnf.conf"

Upgrading Fedora 23
===================

Prerequisites for upgrading
---------------------------

First, we make sure we have enough space on our ``/`` partition, since during
the update process we will need to download the most recent version of each and
every single of the packages installed in our system. Whereas there is a
possibility that our cache may be full, it is good to remove the packages
stored in it to freed space in case we need:

.. code-block:: console

    su -c 'dnf clean all'

Before we continue, we need to make sure that our system has installed the
latest updates available from the different repositories enabled in our system.
To do this, we must reconstruct the packages metadata cache and then apply the
recent upgrades:

.. code-block:: console

    su -c 'dnf makecache'

.. image:: {filename}/images/fc22_to_fc23/screenshot_from_2016-11-22_17-23-27.png
   :align: center

.. code-block:: console

    su -c 'dnf upgrade'

Install the dnf-plugin-system-upgrade plugin
--------------------------------------------

**DNF System Upgrade** can upgrade your system to a more recent version of
Fedora, using a mechanism similar to that used for offline package updates.
Packages are donwloaded while the system is running normally, and then the
system is restarted in a special environment (implemented as a systmend target)
to install them. Once the installation of the packages is complete, the system
reboots but this time in the new Fedora version.

The first step is to install the ``dnf-plugin-system-upgrade`` plugin:

.. code-block:: console

    su -c 'dnf install dnf-plugin-system-upgrade'

And now let's proceed to download the packages needed to upgrade to Fedora 23.

This process will download each and every one of the packages that we have
installed in our system, in its most recent version available for the release
that we indicate, in this case the release will be ``23``.

.. code-block:: console

    su -c 'dnf system-upgrade download --refresh --best --allowerasing --releasever=23'

In the next screenshot you can see the number of packages to download and the
amount of data that implies downloading them:

.. image:: {filename}/images/fc22_to_fc23/screenshot_from_2016-11-22_17-34-42.png
   :align: center

In the same way it is possible to upgrade to Fedora 24, although I do not
recommend jumping to a ``(n + 2)`` Fedora version, that is, moving from Fedora
22 to Fedora 24. At the moment, the most recent stable versions are Fedora 24
and Fedora 25; Fedora 26 is `Branched
<https://fedoraproject.org/wiki/Releases/Branched>`_ and `Rawhide
<https://fedoraproject.org/wiki/Releases/Rawhide>`_ the version in continuous
development. To upgrade to any of the above versions, only the ``number``
parameter should be edited in the ``--releasever=number`` option, 24 for F24,
25 for F25, 26 for Fedora Branched and ``rawhide`` to upgrade to Rawhide. It
should be noted that both Branched and Rawhide are not stable versions of
Fedora, so its use is only recommended for more experienced users.

Upgrading to Fedora 24:

.. code-block:: console

    su -c 'dnf system-upgrade download --refresh --best --allowerasing --releasever=24'

Upgrading to Fedora 25:

.. code-block:: console

    su -c 'dnf system-upgrade download --refresh --best --allowerasing --releasever=25'

Upgrading to Fedora Rawhide:

.. code-block:: console

    su -c 'dnf system-upgrade download --refresh --best --allowerasing --releasever=rawhide'

Finally, once it downloads the packages, it is necessary to restart the system
by executing the following command:

.. code-block:: console

    su -c 'dnf system-upgrade reboot'

This will restart the system. Then the system should boot again using the same
(newer) kernel, but this time it will start the upgrade process from Fedora 22
to Fedora 23.