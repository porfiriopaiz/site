Mate Desktop on Debian
######################

:date: 2021-07-22 19:11
:tags: deb11, debian, mate-desktop
:category: floss
:slug: mate-desktop-on-debian
:summary: Configuration tips and tricks for Mate Desktop on my Debian setup.
:lang: en

Mate Desktop Tips and Tricks
============================

Notify Battery Discharging
---------------------------

Enable notification when the battery is discharging:

.. code-block:: console

   gsettings set org.mate.power-manager notify-discharging true

Enable Window Compositing
-------------------------

Turn on window compositing for better visual effects:

.. code-block:: console

   gsettings set org.mate.Marco.general compositing-manager true

Center New Windows
------------------

Automatically center new windows on the screen:

.. code-block:: console

   gsettings set org.mate.Marco.general center-new-windows true

Enable Window Snapping
----------------------

Allow window snapping for better workspace management:

.. code-block:: console

   gsettings set org.mate.Marco.general allow-tiling true

Hide All Desktop Icons
----------------------

Remove all desktop icons for a cleaner look:

.. code-block:: console

   gsettings set org.mate.background show-desktop-icons false

Customize Window Button Layout
------------------------------

Modify the order of window decoration buttons:

.. code-block:: console

   gsettings set org.mate.Marco.general button-layout 'close,maximize,minimize:menu'

Disable Auto-Mount Open
-----------------------

Prevent the file manager from opening automatically on mounting:

.. code-block:: console

   gsettings set org.mate.media-handling automount-open false

Disable Auto-Mounting
---------------------

Turn off automatic mounting of devices:

.. code-block:: console

   gsettings set org.mate.media-handling automount false

Caja File Manager Preferences
-----------------------------

Set Default Sorting Order
~~~~~~~~~~~~~~~~~~~~~~~~~~

Change the default sorting order to "type":

.. code-block:: console

   gsettings set org.mate.caja.preferences default-sort-order 'type'

Sort Directories First
~~~~~~~~~~~~~~~~~~~~~~

Ensure directories are always sorted first:

.. code-block:: console

   gsettings set org.mate.caja.preferences sort-directories-first true

Customize Appearance
--------------------

Set Icon Theme
~~~~~~~~~~~~~~

Choose an icon theme, e.g., "gnome":

.. code-block:: console

   gsettings set org.mate.interface icon-theme 'gnome'

Set GTK Theme
~~~~~~~~~~~~~

Select a GTK theme, e.g., "Arc-Dark":

.. code-block:: console

   gsettings set org.mate.interface gtk-theme 'Arc-Dark'

Set Window Border Theme
~~~~~~~~~~~~~~~~~~~~~~~

Define the theme for window borders:

.. code-block:: console

   gsettings set org.mate.Marco.general theme 'Arc-Dark'