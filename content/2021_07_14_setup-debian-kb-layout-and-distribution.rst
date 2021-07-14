Setup Debian keyboard layout and distribution
#############################################

:date: 2021-7-14 16:38
:tags: deb11, debian, keyboard, layout, distribution
:category: floss
:slug: setup-debian-kb-layout-and-distribution
:summary: How to setup English International with AltGr dead keys
:lang: en

During the Debian installation process we are offered to setup our keyboard
layout and distribution; sadly my favorite one is not listed as one the
possible options.

I would like to be able to set it up as English International with AltGr dead
keys.

This is something I have to do as a post-install setting by running the next
command:

.. code-block:: console

   su -c 'localectl set-x11-keymap us thinkpad altgr-intl'

This sets the layout as English US; the model compatible with my Lenovo
ThinkPad T440p; the variant as Dead keys via AltGr, which means I can input
characters as á or ñ by just pressing: AltGr + a or AltGr + n respectively. 

.. code-block:: console

   pionen@lilit:~$ localectl 
   System Locale: LANG=en_US.UTF-8
                  LANGUAGE=en_US:en
       VC Keymap: n/a
      X11 Layout: us
       X11 Model: thinkpad
     X11 Variant: altgr-intl

This way I can continue using the English US keyboard layout when writing in
either English or Spanish without having to change the variant or physical
layout.
