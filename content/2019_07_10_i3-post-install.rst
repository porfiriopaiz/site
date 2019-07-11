i3 post install
###############

:date: 2018-12-09 21:26
:tags: dnf, fc29, fedora, postinstall
:category: floss
:slug: i3-post-install
:summary: Fedora 29 i3 window manager post-install
:lang: en

After installing Fedora 29 with i3 window manager, we need to install many
other programs that will ease our user experience.

The first problem we have to solve is how are we going to connect to Internet,
you might have noticed that we don't have any program or applet that allows us
to activate the Wi-Fi card or even the NetworkManager service to use the wired
wetwork card or manage the different networks that are within our reach.

Assuming that you are already logged in and that your hardware is supported by
Fedora, the wireless network card should be activated, but how do we connect to
any of the networks we have available?

nmcli
=====

In the previous post we installed a set of packages provided by the group
"Hardware Support", this group provides support for a wide variety of
networking hardware.  We also install the group of packages corresponding to
NetworkManager.

`` nmcli`` is a command-line program that will allow us to activate by software
the network hardware of our device, scan the networks that are around us and
connect to them.

We will need a terminal, by pressing <Start> + <Enter> we get a Terminal.

If our device has a switch that allows to activate or deactivate the
network card, we make sure it is activated.

Then on the terminal we execute the following command to verify that it is
already activated by software:

.. code-block:: console

   nmcli networking on

This should activate the wired network connection of our device in case we were
accessing one and we wanted to use it.

To activate the wireless network hardware from the terminal, we execute the
following command:

.. code-block:: console

   nmcli radio wifi on

This should activate our network card, then we verify which are the networks
that we have available at our reach:

.. code-block:: console

   nmcli device wifi list

.. code-block:: console

   IN-USE  SSID           MODE   CHAN  RATE        SIGNAL  BARS  SECURITY
           RED_WIFI_2     Infra  5     130 Mbit/s  100     ▂▄▆█  WPA2
           RED_WIFI_2     Infra  1     130 Mbit/s  29      ▂___  WPA2
           RED_WIFI_3     Infra  1     54 Mbit/s   17      ▂___  WPA1

In case you need to scan again to verify other connections:

.. code-block:: console

   nmcli device wifi rescan

Assuming that ``RED_WIFI_1`` does not require an access password, to get
connected we just execute the following command:

.. code-block:: console

   nmcli device wifi connect RED_WIFI_1

In case that we might need to provide a password:

.. code-block:: console

   nmcli device wifi connect RED_WIFI_1 password "1234567890"

Where:

   ``connect`` is the task we want to accomplish.

   ``RED_WIFI_1`` this argument tells the network we want to get connected.

   ``password`` a parameter that tells we are going to provide a password to
   get authenticated.

   ``1234567890`` this is the argument passed for the previous parameter, the
   password of the nextwork. Here you must provided the password that works for
   you.

By now, you should be connected to the network. Now proceed to install any
other program that will help you to ease you user experience with i3.

Networks
========

mn-applet
---------

``nm-applet`` is a very simple applet for NetworkManager that allows us to do
in a very easy and intuitive way what we did with ``nmcli``, but in a graphical
way.

.. code-block:: console

   su -c 'dnf install nm-applet'

To run ``nm-applet`` press <Start> + <d> and type `nm-applet` and press
<Enter>. In the lower right corner of our screen should appear an icon
corresponding to this `applet` from where we can manage our connection to the
different networks that we have available to around us.

NetworkManager-tui
------------------

This is an alternative for ``nm-applet`` that make use of ``ncurses`` to create
a very friendly `Text User Interface`.

.. code-block:: console

   su -c 'dnf install NetworkManager-tui'

nm-connecion-editor
-------------------

`NetworkManager Connection Editor` allows us to edit in a friendly way and
intuitively the different networks to which we have accessed, or Well, create
Hotspots in case our network card supports it.

.. code-block:: console

   su -c 'dnf install nm-connection-editor'

Terminal Emulator
=================

You may have noticed that the emulator that is installed by default with i3 is
``rxvt-unicode`` and that is not very friendly to say, it is not very
intuitive to first sight and it has a certain learning curve that we do not
want to go through, possibly...

Ironically, my favorite terminal emulator is GNOME Terminal, you can install
the one you prefer.

.. code-block:: console

   su -c 'dnf install gnome-terminal'

``i3`` has the key combination <Start> + <Enter> assigned to the emulator
``urxvt``, to launch GNOME Terminal instead, you need to edit the configuration
file for  ``i3`` (``~ /.config/i3/config``), look for the line:

.. code-block:: console

   bindsym $mod+Return exec i3-sensible-terminal

And replace with the command that calls our terminal emulator, in my case,
``gnome-terminal``:

.. code-block:: console

   bindsym $mod+Return exec gnome-terminal

In the following post I will share what other programs I use in my setup Fedora
29 with i3wm. At the moment you already have the necessary to install other
interesting programs such as Web browser and others.
