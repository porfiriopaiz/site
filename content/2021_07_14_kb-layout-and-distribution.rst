Setup Debian Keyboard Layout and Distribution
##############################################

:date: 2021-07-14 16:38
:tags: deb11, debian, distribution, keyboard, layout
:category: floss
:slug: kb-layout-and-distribution
:summary: How to set up English International with AltGr dead keys
:lang: en

During the Debian installation process, we are prompted to set up our keyboard
layout and distribution. Unfortunately, my preferred layout is not listed as
one of the available options.

I would like to set it up as English International with AltGr dead keys.

This is something I need to configure as a post-installation setting by running
the following command:

.. code-block:: console

   su -c 'localectl set-x11-keymap us thinkpad altgr-intl'

This sets the layout to English (US), the model to one compatible with my
Lenovo ThinkPad T440p, and the variant to Dead keys via AltGr. This allows me
to input characters such as á or ñ by simply pressing: AltGr + a or AltGr + n,
respectively.

.. code-block:: console

   pionen@lilit:~$ localectl 
   System Locale: LANG=en_US.UTF-8
                  LANGUAGE=en_US:en
       VC Keymap: n/a
      X11 Layout: us
       X11 Model: thinkpad
     X11 Variant: altgr-intl

This way, I can continue using the English (US) keyboard layout when typing in
either English or Spanish without needing to change the variant or physical
layout.
