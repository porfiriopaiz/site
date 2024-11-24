i3 Post-Install
###############

:date: 2018-12-09 21:26
:tags: dnf, fc29, fedora, postinstall
:category: floss
:slug: i3-post-install
:summary: Fedora 29 i3 Window Manager Post-Install
:lang: en

After installing Fedora 29 with the i3 Window Manager, additional programs are
necessary to enhance the user experience.

The first issue to address is how to connect to the Internet. You may have
noticed that there is no program or applet to activate the Wi-Fi card or manage
the NetworkManager service for a wired network card or available networks.

Assuming you are logged in and your hardware is supported by Fedora, the
wireless network card should already be activated. But how do you connect to
the networks within range?

nmcli
=====

In a previous post, we installed a set of packages from the "Hardware Support"
group. This group provides support for various networking hardware. We also
installed the package group for NetworkManager.

``nmcli`` is a command-line utility that allows us to activate network
hardware, scan for available networks, and connect to them.

To get started, open a terminal by pressing <Start> + <Enter>.

Ensure your device’s physical network card switch (if present) is enabled.
Then, in the terminal, verify that networking is activated via software with
the following command:

.. code-block:: console

   nmcli networking on

This will activate the wired network connection if available and ready for use.

To activate the wireless network hardware, execute:

.. code-block:: console

   nmcli radio wifi on

This activates the wireless card. Next, scan for available networks:

.. code-block:: console

   nmcli device wifi list

Example output:

.. code-block:: console

   IN-USE  SSID           MODE   CHAN  RATE        SIGNAL  BARS  SECURITY
           RED_WIFI_1     Infra  5     130 Mbit/s  100     ▂▄▆█  WPA2
           RED_WIFI_2     Infra  1     130 Mbit/s  29      ▂___  WPA2
           RED_WIFI_3     Infra  1     54 Mbit/s   17      ▂___  WPA1

To refresh the network list, use:

.. code-block:: console

   nmcli device wifi rescan

If the network ``RED_WIFI_1`` does not require a password, connect using:

.. code-block:: console

   nmcli device wifi connect RED_WIFI_1

For networks requiring a password, use:

.. code-block:: console

   nmcli device wifi connect RED_WIFI_1 password "1234567890"

Explanation of parameters:

- ``connect`` specifies the task to perform.
- ``RED_WIFI_1`` identifies the target network.
- ``password`` indicates that a password will be provided.
- ``1234567890`` is the password (replace with your network’s password).

You should now be connected to the network. Next, install programs to improve
your experience with i3.

Networks
========

nm-applet
---------

``nm-applet`` is a simple graphical applet for NetworkManager. It provides an
intuitive interface for managing network connections.

Install it with:

.. code-block:: console

   su -c 'dnf install nm-applet'

To launch ``nm-applet``, press <Start> + <d>, type `nm-applet`, and press
<Enter>. An icon should appear in the lower-right corner of your screen for
managing network connections.

NetworkManager-tui
------------------

``NetworkManager-tui`` is an alternative to ``nm-applet`` that uses ``ncurses``
to create a user-friendly Text User Interface.

Install it with:

.. code-block:: console

   su -c 'dnf install NetworkManager-tui'

nm-connection-editor
--------------------

The `NetworkManager Connection Editor` provides an intuitive interface for
editing saved networks or creating hotspots (if supported by your network
card).

Install it with:

.. code-block:: console

   su -c 'dnf install nm-connection-editor'

Terminal Emulator
=================

The default terminal emulator installed with i3 is ``rxvt-unicode``
(``urxvt``). While powerful, it can be unintuitive and has a steep learning
curve.

If you prefer a more user-friendly terminal emulator, such as GNOME Terminal,
you can install it with:

.. code-block:: console

   su -c 'dnf install gnome-terminal'

To set GNOME Terminal as the default terminal for <Start> + <Enter>, edit the
i3 configuration file (``~/.config/i3/config``). Look for the line:

.. code-block:: console

   bindsym $mod+Return exec i3-sensible-terminal

Replace it with:

.. code-block:: console

   bindsym $mod+Return exec gnome-terminal

In the next post, I will share other programs I use in my Fedora 29 i3wm setup.
For now, you should have the tools necessary to install additional programs,
such as a web browser.
