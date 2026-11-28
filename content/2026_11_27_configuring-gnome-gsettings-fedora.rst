Configuring GNOME, Nautilus, and Power Management via CLI on Fedora
###################################################################

:date: 2026-11-27 23:00
:tags: busctl, cli, dconf, fedora, gnome, gsettings, linux, nautilus, systemd
:category: floss
:slug: configuring-gnome-nautilus-power-cli-fedora
:summary: A practical guide on discovering, inspecting, and setting GNOME
          desktop preferences, Nautilus sorting behavior, battery charge
          thresholds, and lid-close policies from the command line on
          Fedora Linux.
:lang: en

On Fedora Linux with the GNOME desktop, hardware, interface, file manager,
and power management settings are distributed across GSettings schemas,
D-Bus interfaces, and ``systemd-logind``. Rather than clicking through
graphical menus, you can discover the exact schema paths, inspect valid
key ranges, monitor live changes, and script reproducible workstation
setups directly from the terminal.

----

Discovering Schemas, Keys, and Valid Values
===========================================

Before modifying any setting, you can query GNOME's GSettings database to
locate the right schema, read key documentation, check allowed data types
or enum values, and watch changes in real time.

Step 1: Search for Relevant Schemas
-----------------------------------

List all available schemas and filter them by keyword:

.. code-block:: bash

   gsettings list-schemas | grep -i "power"

Alternatively, search recursively across all schemas and current values
simultaneously:

.. code-block:: bash

   gsettings list-recursively | grep -i touchpad

Step 2: Inspect Keys and Current Values
---------------------------------------

Once you have a schema name, list its available keys or print every key
alongside its active value:

.. code-block:: bash

   # List only key names in a schema
   gsettings list-keys org.gnome.desktop.peripherals.touchpad

.. code-block:: bash

   # List all keys and their current values
   gsettings list-recursively org.gnome.desktop.peripherals.touchpad

Step 3: Read Key Descriptions and Allowed Ranges
------------------------------------------------

To avoid invalid value errors, inspect a key's built-in description and
check the exact values or range it accepts (booleans, integers, or string
enums):

.. code-block:: bash

   # Read a key's description
   gsettings describe org.gnome.desktop.peripherals.touchpad two-finger-scrolling-enabled

.. code-block:: bash

   # Check valid values or range for a specific key
   gsettings range org.gnome.desktop.peripherals.touchpad scroll-method

Step 4: Monitor Live Changes from the GUI
-----------------------------------------

If you want to identify which key a toggle in the Fedora **Settings** app
modifies, run ``gsettings monitor`` on a schema and click the option in
the GUI:

.. code-block:: bash

   gsettings monitor org.gnome.desktop.peripherals.touchpad

Common GSettings Schemas Reference
----------------------------------

+--------------------+--------------------------------------------+
| Feature            | GSettings Schema                           |
+====================+============================================+
| Touchpad           | ``org.gnome.desktop.peripherals.touchpad`` |
+--------------------+--------------------------------------------+
| Mouse              | ``org.gnome.desktop.peripherals.mouse``    |
+--------------------+--------------------------------------------+
| Keyboard           | ``org.gnome.desktop.peripherals.keyboard`` |
+--------------------+--------------------------------------------+
| Interface / Fonts  | ``org.gnome.desktop.interface``            |
+--------------------+--------------------------------------------+
| Power Management   | ``org.gnome.settings-daemon.plugins.power``|
+--------------------+--------------------------------------------+
| Privacy / Lock     | ``org.gnome.desktop.screensaver``          |
+--------------------+--------------------------------------------+
| Window Focus       | ``org.gnome.desktop.wm.preferences``       |
+--------------------+--------------------------------------------+
| File Manager       | ``org.gnome.nautilus.preferences``         |
+--------------------+--------------------------------------------+

----

Touchpad and Mouse Configuration
================================

On a laptop such as a Lenovo ThinkPad, configuring tap-to-click,
two-finger scrolling, and natural scrolling across both the touchpad and
external mice is handled under ``org.gnome.desktop.peripherals``.

Touchpad Preferences
--------------------

* **Schema:** ``org.gnome.desktop.peripherals.touchpad``

.. code-block:: bash

   # Enable tap-to-click
   gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click true

.. code-block:: bash

   # Enable Natural Scrolling (reverse scroll)
   gsettings set org.gnome.desktop.peripherals.touchpad natural-scroll true

.. code-block:: bash

   # Enable two-finger scrolling
   gsettings set org.gnome.desktop.peripherals.touchpad two-finger-scrolling-enabled true

Mouse Preferences
-----------------

* **Schema:** ``org.gnome.desktop.peripherals.mouse``

.. code-block:: bash

   # Inspect all mouse keys and current values
   gsettings list-recursively org.gnome.desktop.peripherals.mouse

.. code-block:: bash

   # Enable natural scrolling for an external mouse
   gsettings set org.gnome.desktop.peripherals.mouse natural-scroll true

----

Panel Indicators and Color Schemes
==================================

GNOME refers to the top bar as the **Panel** and the application dock as
the **Dash**. System-wide appearance, clock details, and battery
percentage indicators live under ``org.gnome.desktop.interface``, while
extensions such as Dash to Dock use ``org.gnome.shell.extensions.dash-to-dock``.

Top Panel Clock and Battery Readouts
------------------------------------

.. code-block:: bash

   # Show the day of the week alongside date/time
   gsettings set org.gnome.desktop.interface show-datetime-day-of-week true

.. code-block:: bash

   # Show seconds in the clock
   gsettings set org.gnome.desktop.interface clock-show-seconds true

.. code-block:: bash

   # Show battery percentage
   gsettings set org.gnome.desktop.interface show-battery-percentage true

Switching Between Dark and Light Themes
---------------------------------------

The ``color-scheme`` key under ``org.gnome.desktop.interface`` controls
GNOME's system-wide dark and light appearance:

.. code-block:: bash

   # Activate Dark Mode
   gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'

.. code-block:: bash

   # Revert to Light / Default Mode
   gsettings set org.gnome.desktop.interface color-scheme 'default'

.. code-block:: bash

   # Check the currently active theme mode
   gsettings get org.gnome.desktop.interface color-scheme

You can also toggle between both modes automatically in a script or alias:

.. code-block:: bash

   CURRENT=$(gsettings get org.gnome.desktop.interface color-scheme)
   if [ "$CURRENT" = "'prefer-dark'" ]; then
       gsettings set org.gnome.desktop.interface color-scheme 'default'
   else
       gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'
   fi

----

Configuring Nautilus Sorting and Folders First
==============================================

Nautilus schema keys have evolved across recent GNOME and GTK releases.
Folder-first sorting is managed upstream at the GTK FileChooser level
rather than as a standalone ``folders-first`` key inside Nautilus.

Inspecting Nautilus and GTK FileChooser Keys
--------------------------------------------

.. code-block:: bash

   # Inspect Nautilus preference keys and valid sort orders
   gsettings list-recursively org.gnome.nautilus.preferences
   gsettings range org.gnome.nautilus.preferences default-sort-order

.. code-block:: bash

   # Locate all directory-sorting keys across schemas
   gsettings list-recursively | grep -iE "sort|folder"

Setting Sort Order and Enforcing Folders First
----------------------------------------------

Configure Nautilus to sort by file type in ascending order, and enable
``sort-directories-first`` across both GTK 3 and GTK 4 schemas:

.. code-block:: bash

   # Sort files by type in ascending order
   gsettings set org.gnome.nautilus.preferences default-sort-order 'type'
   gsettings set org.gnome.nautilus.preferences default-sort-in-reverse-order false

.. code-block:: bash

   # Enable folders-first sorting in GTK 3 and GTK 4 FileChooser schemas
   gsettings set org.gtk.Settings.FileChooser sort-directories-first true
   gsettings set org.gtk.gtk4.Settings.FileChooser sort-directories-first true

If a GTK schema is not exposed directly to ``gsettings`` in your current
session, write the underlying keys using ``dconf``:

.. code-block:: bash

   dconf write /org/gtk/settings/file-chooser/sort-directories-first true
   dconf write /org/gtk/gtk4/settings/file-chooser/sort-directories-first true

Applying Changes Globally
-------------------------

Restart Nautilus and clear cached per-folder GVfs metadata so the new
defaults apply recursively across all directories:

.. code-block:: bash

   nautilus -q
   rm -rf ~/.local/share/gvfs-metadata

----

Power Management, Battery Thresholds, and Lid Switch Policies
=============================================================

Power behavior on modern Fedora GNOME systems spans three subsystems:
``gsettings`` for idle sleep timeouts, UPower over D-Bus (``busctl``) for
battery charge thresholds, and ``systemd-logind`` for physical lid-switch
events.

Idle Sleep and Suspend Timeouts (``gsettings``)
-----------------------------------------------

Control inactive sleep timeouts and automatic suspend actions via
``org.gnome.settings-daemon.plugins.power``:

.. code-block:: bash

   # Inspect current sleep and suspend settings
   gsettings list-recursively org.gnome.settings-daemon.plugins.power | grep sleep

.. code-block:: bash

   # Set sleep timeout on battery (in seconds, e.g., 900 = 15 minutes)
   gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-timeout 900

.. code-block:: bash

   # Disable automatic suspend on AC power and battery
   gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing'
   gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type 'nothing'

To prevent the GDM login screen from suspending automatically while idle:

.. code-block:: bash

   sudo -u gdm dbus-run-session gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing'

Battery Charging Thresholds (``busctl`` / UPower)
-------------------------------------------------

.. note::
   GNOME's native **Preserve Battery Health** vs. **Maximize Charge**
   option does not use a ``gsettings`` key; instead, it communicates
   directly with UPower over D-Bus.

First, locate your battery's UPower device path and inspect its supported
methods:

.. code-block:: bash

   upower -e | grep battery
   busctl introspect org.freedesktop.UPower /org/freedesktop/UPower/devices/battery_BAT0

Toggle the charge threshold (replace ``battery_BAT0`` if your system uses
a different battery identifier):

.. code-block:: bash

   # Enable "Preserve Battery Health" (caps charge around 80%)
   busctl call org.freedesktop.UPower /org/freedesktop/UPower/devices/battery_BAT0 org.freedesktop.UPower.Device EnableChargeThreshold b true

.. code-block:: bash

   # Set to "Maximize Charge" (allows charging to 100%)
   busctl call org.freedesktop.UPower /org/freedesktop/UPower/devices/battery_BAT0 org.freedesktop.UPower.Device EnableChargeThreshold b false

Preventing Sleep on Laptop Lid Close (``systemd-logind``)
---------------------------------------------------------

.. note::
   Modern GNOME releases removed lid-close action keys from ``gsettings``
   (such as ``lid-close-ac-action``) and delegate hardware lid-switch
   handling directly to ``systemd-logind``.

To permanently ignore lid-close events across battery, AC power, and
docked states, create a drop-in configuration file for ``systemd-logind``:

.. code-block:: bash

   sudo mkdir -p /etc/systemd/logind.conf.d
   sudo tee /etc/systemd/logind.conf.d/lid.conf << 'EOF'
   [Login]
   HandleLidSwitch=ignore
   HandleLidSwitchExternalPower=ignore
   HandleLidSwitchDocked=ignore
   EOF

Restart ``systemd-logind`` to apply the policy immediately (note that
restarting ``systemd-logind`` may terminate your active graphical session):

.. code-block:: bash

   sudo systemctl restart systemd-logind

If you only want to prevent sleep temporarily while a specific task runs,
use ``systemd-inhibit`` instead of modifying system configuration files:

.. code-block:: bash

   systemd-inhibit --what=handle-lid-switch sleep 3600

----

Finishing Touches
=================

Combining ``gsettings``, ``dconf``, ``busctl``, and ``systemd-logind``
gives you complete command-line control over your Fedora GNOME workstation,
making it straightforward to version-control and replicate your exact
desktop, file manager, and power configuration across fresh installs.
