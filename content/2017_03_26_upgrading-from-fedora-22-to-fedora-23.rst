Upgrading from Fedora 22 to Fedora 23
#####################################

:date: 2017-3-26 16:46
:tags: dnf, eol, fc22, fc23, fedora, system-upgrade
:category: floss
:slug: upgrading-from-fedora-22-to-fedora-23
:summary:
:lang: en

From May 26th, 2015, to November 22nd, 2016, I was rocking Fedora 22 on my
Lenovo ThinkPad T440p – a solid year and a half of tech bliss. However, on July
19th, 2016, Fedora 22 gracefully entered its `End of Life (EOL)
<https://fedoraproject.org/wiki/End_of_life>`_ phase. This translates to no
more security or maintenance updates coming our way, signaling the friendly
nudge to upgrade to a newer, stable version.

So, in this post, I'm spilling the beans on how to smoothly transition to
Fedora 23 using the ever-reliable dnf package manager. Let's keep that Fedora
love alive and kicking! 🚀

.. TEASER_END

Following a year and a half of utilizing Fedora 22, the package cache had
accumulated roughly 10GB of space on my hard drive.

.. image:: {filename}/images/fc22_to_fc23/screenshot_from_2016-11-22_16-05-06.png
   :align: center

To instruct dnf to retain the downloaded packages in the cache, you need to
append the following line to the dnf configuration file located at
``/etc/dnf/dnf.conf``:

.. code-block:: console

    su -c "echo 'keepcache = true' >> /etc/dnf/dnf.conf"

Upgrading Fedora 23
===================

Prerequisites for upgrading
---------------------------

Firstly, it's crucial to ensure ample space on our ``/`` partition. This is
particularly important because the update process entails downloading the
latest version of every single package installed in our system. While there's a
chance that our cache might be brimming, it's advisable to clear out stored
packages to free up space, just in case it's needed:

.. code-block:: console

    su -c 'dnf clean all'

Before we proceed, it's essential to verify that our system is up-to-date with
the latest available updates from the enabled repositories. To accomplish this,
we need to rebuild the packages' metadata cache and subsequently apply the
recent upgrades:

.. code-block:: console

    su -c 'dnf makecache'

.. image:: {filename}/images/fc22_to_fc23/screenshot_from_2016-11-22_17-23-27.png
   :align: center

.. code-block:: console

    su -c 'dnf upgrade'

Install the dnf-plugin-system-upgrade plugin
--------------------------------------------

**DNF System Upgrade** facilitates the transition to a newer version of Fedora,
employing a mechanism akin to offline package updates. Packages are downloaded
while the system operates normally, followed by a restart into a dedicated
environment (implemented as a systemd target) for installation. Once the
package installation concludes, the system reboots, ushering in the new Fedora
version.

To kickstart the process, the initial step involves installing the
``dnf-plugin-system-upgrade`` plugin:

.. code-block:: console

    su -c 'dnf install dnf-plugin-system-upgrade'

Now, let's move on to acquiring the necessary packages for the upgrade to
Fedora 23.

This operation entails fetching each and every package currently installed in
our system, ensuring we obtain the latest version compatible with the specified
release – in this instance, the release is designated as ``23``.

.. code-block:: console

    su -c 'dnf system-upgrade download --refresh --best --allowerasing --releasever=23'

In the following screenshot, you'll find details on the number of packages
slated for download and the corresponding data volume associated with fetching
them:

.. image:: {filename}/images/fc22_to_fc23/screenshot_from_2016-11-22_17-34-42.png
   :align: center

Similarly, upgrading to Fedora 24 is feasible, although I would advise against
leaping directly from Fedora 22 to Fedora 24 (a ``(n + 2)`` version jump). As
of now, the latest stable versions are Fedora 24 and Fedora 25; Fedora 26 is
currently in the `Branched <https://fedoraproject.org/wiki/Releases/Branched>`_
state, and `Rawhide <https://fedoraproject.org/wiki/Releases/Rawhide>`_
represents the continuously developing version.

To transition to any of the mentioned versions, you simply need to modify the
``number`` parameter in the ``--releasever=number`` option. Use 24 for Fedora
24, 25 for Fedora 25, 26 for Fedora Branched, and "rawhide" to upgrade to
Rawhide. It's worth noting that both Branched and Rawhide are not stable
versions of Fedora, so their use is recommended primarily for more seasoned
users.

Upgrading to Fedora 24:

.. code-block:: console

    su -c 'dnf system-upgrade download --refresh --best --allowerasing --releasever=24'

Upgrading to Fedora 25:

.. code-block:: console

    su -c 'dnf system-upgrade download --refresh --best --allowerasing --releasever=25'

Upgrading to Fedora Rawhide:

.. code-block:: console

    su -c 'dnf system-upgrade download --refresh --best --allowerasing --releasever=rawhide'

Lastly, after the packages are successfully downloaded, it's imperative to
restart the system by executing the following command:

.. code-block:: console

    su -c 'dnf system-upgrade reboot'

Executing this command initiates a system restart. Upon reboot, the system will
utilize the same (newer) kernel, triggering the upgrade process from Fedora 22
to Fedora 23.
