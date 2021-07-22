Mate Desktop on Debian
######################

:date: 2021-7-22 19:11
:tags: deb11, debian, mate-desktop
:category: floss
:slug: mate-desktop-on-debian
:summary: Mate Desktop config on my Debian setup
:lang: en

Mate Desktop Tips and Tricks
============================

Notify discharging of the battery:

.. code-block:: console

   gsettings set org.mate.power-manager notify-discharging true

Enable windows composing:

.. code-block:: console

   gsettings set org.mate.Marco.general compositing-manager true

Enable new window centering:

.. code-block:: console

   gsettings set org.mate.Marco.general center-new-windows true

Enable window snapping:

.. code-block:: console

   gsettings set org.mate.Marco.general allow-tiling true

Hide all desktop icons:

.. code-block:: console

   gsettings set org.mate.background show-desktop-icons false

Change window decoration button order:

.. code-block:: console

   gsettings set org.mate.Marco.general button-layout 'close,maximize,minimize:menu'

Disable automount-open:

.. code-block:: console

   gsettings set org.mate.media-handling automount-open false

Disable automounting:

.. code-block:: console

   gsettings set org.mate.media-handling automount false

Caja default prefereces for sorting order:

.. code-block:: console

   gsettings set org.mate.caja.preferences default-sort-order 'type'

Caja sort directories first:

.. code-block:: console

   gsettings set org.mate.caja.preferences sort-directories-first true

Set icon theme:

.. code-block:: console

   gsettings set org.mate.interface icon-theme 'gnome'

Set GTK theme:

.. code-block:: console

   gsettings set org.mate.interface gtk-theme 'Arc-Dark'

Set GTK windows border theme:

.. code-block:: console

   gsettings set org.mate.Marco.general theme 'Arc-Dark'
