Keeping Your APT Package Cache Persistent
#########################################

:date: 2026-02-01 15:00
:tags: apt, cache, debian, systemd
:category: floss
:slug: keep-apt-cache
:summary: How to prevent Debian from automatically clearing the 
          /var/cache/apt/archives directory and disable automated updates.
:lang: en

If ``/var/cache/apt/archives`` is empty, it usually means your system is 
configured to clean up automatically to save disk space. While this keeps the 
system lean, it’s frustrating if you wanted to keep those .deb files for 
backups or offline installs.

Here is how to find the culprit and fix it.

----

Check the "Keep-Downloaded-Packages" Setting
--------------------------------------------

Modern Debian/Ubuntu systems often have a specific configuration that deletes 
packages immediately after installation. You need to ensure this is set to 
``true``.

You can create or edit the configuration file using this ``sed`` command:

.. code-block:: bash

   sudo touch /etc/apt/apt.conf.d/01keep-debs && sudo sed -i '1i Binary::apt::APT::Keep-Downloaded-Packages "true";' /etc/apt/apt.conf.d/01keep-debs # Force APT to retain downloaded .deb files

.. note::
   If this is set to ``false`` (or ``0``), APT deletes the files as soon as the 
   installation finishes.

----

Disable Periodic Cleaning and Automation
----------------------------------------

Debian has a background service called ``apt-daily`` that handles automated package maintenance. Even if you tell APT to keep files, the daily maintenance script might be sweeping them away. Modern versions rely on **systemd timers** rather than traditional cron jobs.

Understanding APT Timers
^^^^^^^^^^^^^^^^^^^^^^^^

The key components are:

* **apt-daily.timer**: Triggers the background refresh of package lists.
* **apt-daily-upgrade.timer**: Triggers the actual download and installation of updates.

Check the status of these timers with:

.. code-block:: bash

   systemctl status apt-daily.timer # Verify if the daily refresh timer is active

Manual Configuration via APT Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To ensure configurations are applied regardless of the current state of the file, we use a logic that checks for the file's existence, creates it if missing, and ensures the specific lines are either updated or appended.

For the standard periodic settings in ``10periodic``, use the following block:

.. code-block:: bash

   FILE=/etc/apt/apt.conf.d/10periodic
   sudo touch $FILE
   grep -q "APT::Periodic::MaxAge" $FILE && sudo sed -i 's/APT::Periodic::MaxAge ".*"/APT::Periodic::MaxAge "0";/' $FILE || echo 'APT::Periodic::MaxAge "0";' | sudo tee -a $FILE
   grep -q "APT::Periodic::MaxSize" $FILE && sudo sed -i 's/APT::Periodic::MaxSize ".*"/APT::Periodic::MaxSize "0";/' $FILE || echo 'APT::Periodic::MaxSize "0";' | sudo tee -a $FILE

This logic ensures that if the file is missing, it is created; if the lines exist, they are edited to "0"; and if the file exists but lacks these lines, they are appended.

Next, to explicitly force the deactivation of all automated functions, create or update the ``20auto-upgrades`` file:

.. code-block:: bash

   sudo tee /etc/apt/apt.conf.d/20auto-upgrades <<EOF
   APT::Periodic::Update-Package-Lists "0";
   APT::Periodic::Download-Upgradeable-Packages "0";
   APT::Periodic::AutocleanInterval "0";
   APT::Periodic::Unattended-Upgrade "0";
   EOF

Deactivating Systemd Timers
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Even with the configurations set to zero, systemd timers will still attempt to trigger services. To stop these triggers entirely:

.. code-block:: bash

   sudo systemctl disable --now apt-daily.timer apt-daily-upgrade.timer # Stop and disable background APT timers

Final Verification
^^^^^^^^^^^^^^^^^^

To confirm that the system will no longer perform automated actions, execute:

1. **Check APT Configuration**:
   ``apt-config dump | grep Periodic`` (All variables should be "0").
2. **Check Active Timers**:
   ``systemctl list-timers | grep apt`` (Should return no results).

----

Check for "No-Cache" Configuration
----------------------------------

Some cloud-images or "minimal" installs include a file that redirects the 
cache to ``/dev/null``. 

Identify Problematic Files
^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if you have a file named ``/etc/apt/apt.conf.d/docker-clean`` (even if 
you aren't in a Docker container) or similar. If you see that line, you can 
comment it out using ``sed``:

.. code-block:: bash

   [ -f /etc/apt/apt.conf.d/docker-clean ] && sudo sed -i '/Dir::Cache::Archives/s/^/#/' /etc/apt/apt.conf.d/docker-clean # Deactivate dev/null redirect

----

Verify Directory Permissions
----------------------------

If the directory permissions are incorrect, APT cannot write the files there. Ensure the directory is owned by **root** but accessible to the **_apt** user.

Run the following to reset permissions:

.. code-block:: bash

   sudo chown root:root /var/cache/apt/archives
   sudo chmod 755 /var/cache/apt/archives
   sudo mkdir -p /var/cache/apt/archives/partial

----

Summary of the APT Cache Path
-----------------------------

+-----------------------------------+-----------------------------------------+
| Folder                            | Purpose                                 |
+===================================+=========================================+
| /var/cache/apt/archives           | Where completed .deb downloads are      |
|                                   | stored.                                 |
+-----------------------------------+-----------------------------------------+
| /var/cache/apt/archives/partial   | Where files sit during the download     |
|                                   | process.                                |
+-----------------------------------+-----------------------------------------+

----

How to Test Your Changes
------------------------

After making these changes, try downloading a package without installing it 
to verify the cache is working:

.. code-block:: bash

   sudo apt update
   sudo apt install --download-only wget
   ls /var/cache/apt/archives | grep wget

By following these steps, you gain absolute manual control over your system,
preventing unexpected resource blocks and ensuring your local package archive
remains persistent for offline use!
