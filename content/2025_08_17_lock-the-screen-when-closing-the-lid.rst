Lock the screen when closing the lid
####################################

:date: 2025-8-17 19:47
:tags: macOS
:category: misc
:slug: lock-the-screen-when-closing-the-lid
:summary: Lock screen upon closing the lid
:lang: en

By default, your MacBook is designed to go to sleep when you close the
lid. When it wakes up, it requires your password (or Touch ID/Apple
Watch) if you have the "Require password" setting enabled for your lock
screen.

Here's how to ensure your MacBook locks when the lid is closed, and some
related settings you might want to consider:

1. Ensure "Require password" is set to "Immediately"
====================================================

This is the most crucial setting for locking your Mac.

For macOS Ventura and later:
----------------------------

* Click the **Apple menu** in the top-left corner of your screen.
* Select **System Settings**.
* Click on **Lock Screen** in the sidebar.
* Next to "Require password after screen saver begins or display is
  turned off," choose **"Immediately"** from the dropdown menu.

For macOS Monterey and earlier:
-------------------------------

* Click the **Apple menu** in the top-left corner of your screen.
* Select **System Preferences**.
* Click on **Security & Privacy**.
* Go to the **General** tab.
* Check the box next to "Require password [time] after sleep or screen
  saver begins."
* From the dropdown menu, select **"immediately."**

----

2. Understanding "Clamshell Mode" (and why it might prevent locking)
====================================================================

If you're using an external monitor, keyboard, and mouse, macOS has a
feature called **"clamshell mode."** In this mode, your MacBook can
remain awake and drive the external display even with the lid closed,
provided it's plugged into power.

If your Mac isn't locking when you close the lid and you're using an
external display, it's likely in clamshell mode. To ensure it locks when
the lid is closed in this scenario, you'd typically either:

* **Manually lock it before closing the lid:** Press **Control +
  Command + Q** to lock the screen.
* **Put it to sleep before closing the lid:** Go to the **Apple menu**
  and select **"Sleep."**

----

3. Adjusting Display Sleep Settings (less about locking, more about power)
==========================================================================

While not directly about locking, you can configure how quickly your
display turns off (which can then trigger the password requirement if
set to "immediately").

For macOS Ventura and later:
----------------------------

* Go to **System Settings > Lock Screen.**
* Adjust "Turn display off on battery when inactive" and "Turn display
  off on power adapter when inactive" to your preferred times. Setting
  them to a shorter time will make your display turn off sooner, and if
  "Require password immediately" is set, it will lock faster.

For macOS Monterey and earlier:
-------------------------------

* Go to **System Preferences > Battery** (or Energy Saver for desktops).
* In the **"Battery"** and **"Power Adapter"** tabs, adjust the "Turn
  display off after" slider.

----

In summary: The key to having your MacBook lock when the lid is closed
is to ensure your "Require password after screen saver begins or display
is turned off" setting is set to **"Immediately."** If you're using an
external monitor in clamshell mode, your Mac might not go to sleep (and
thus lock) automatically, so manual locking or sleeping might be
necessary.
