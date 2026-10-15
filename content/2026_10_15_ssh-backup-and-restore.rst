Backing Up and Restoring SSH Keys
#################################

:date: 2026-10-15 1:04
:tags: fc44, fedora, ssh, security, backup, post-install
:category: floss
:slug: ssh-backup-and-restore
:summary: A practical guide on securely backing up, restoring, and hardening
          OpenSSH keys from .ssh to an external USB on Fedora 44.
:lang: en

When setting up a fresh system like my Lenovo ThinkPad T450 (named
``taylor``) running Fedora Linux 44 (Workstation Edition), transferring
cryptographic identities safely is a top priority. When hardening SSH, the
strictness of file permissions is enforced directly by OpenSSH's
``StrictModes`` check. If permissions are too open, SSH will
reject key usage with errors like permissions being too open.

----

OpenSSH Permission Requirements
===============================

Here are the minimal and recommended permissions required for secure SSH
key directory and file operations on your system.

The SSH Directory (`~/.ssh`)
----------------------------

- **Minimal/Recommended Permission:** ``700`` (`drwx------`).
- **Access Level:** Only the file owner can read, write, and execute the
  directory, leaving group and others with zero access.
- **Ownership:** Must be owned by the active user account utilizing the
  keys.

.. code-block:: bash

   chmod 700 ~/.ssh
   chown -R $USER:$USER ~/.ssh

Files Within the SSH Directory
------------------------------

Permissions vary depending on whether the file contains private data,
public data, or configuration settings:

- **Private Keys** (`id_ed25519`, `id_rsa`): Mode ``600`` (or ``400``) for
  owner read/write or read-only access, barring all others.
- **Public Keys** (`id_ed25519.pub`, `id_rsa.pub`): Mode ``644`` allowing
  owner read/write and group/others read-only access.
- **Authorized Keys** (`authorized_keys`): Mode ``600`` for owner
  read/write only.
- **Config / Known Hosts** (`config`, `known_hosts`): Mode ``600``.

.. note::
   For private key files, the absolute minimum required permission for
   standard SSH operations is ``400`` (`-r--------`). However,
   ``600`` is standard because it allows updating configurations without
   modifying permission bits first.

Parent Directory Constraints
----------------------------

OpenSSH also validates the permissions of parent directories in the path
leading up to ``~/.ssh``. Your home directory must not be
writable by group or world, with a maximum allowable mode of ``755`` or
``750``. If the home directory has overly open permissions, SSH
will refuse key authentication even if ``~/.ssh`` is set to ``700``.

.. code-block:: bash

   chmod 750 /home/$USER

----

Backing Up and Restoring via External USB
=========================================

To transfer your ``.ssh`` directory to an external USB drive from Fedora
44 and later restore it to ``taylor``, standard copying tools can cause
ownership mismatches or strip permission bits. Using ``rsync``
with the ``-p`` (`--perms`) flag ensures permission bits transfer
intact while writing files directly under your current logged-in user.

Using `rsync` for Backup and Restoration
----------------------------------------

Assuming your USB directory mount path points to your target location, run
the copy operation while preserving permissions:

.. code-block:: bash

   rsync -rp /path/to/source/.ssh/ /path/to/destination/.ssh/

The flag breakdown includes:

- **`-r` (`--recursive`):** Recurses into subdirectories and copies all
  files.
- **`-p` (`--perms`):** Preserves explicit file permission modes.
- **No `-o`/`-g`:** Running as a normal user without ``sudo`` automatically
  assigns your current ``$USER`` and primary group as the owner.

Alternative Using `cp`
----------------------

If ``rsync`` is not available, you can perform the copy with ``cp``:

.. code-block:: bash

   cp -r --preserve=mode /path/to/source/.ssh /path/to/destination/.ssh

----

Post-Restore Verification and Hardening
=======================================

After restoring your keys to ``taylor`` from the USB drive, perform a
post-copy safety check and apply mass hardening commands to satisfy OpenSSH
strict mode checks.

Inspection and Hardening Commands
---------------------------------

Verify file permissions and apply the mass hardening script:

.. code-block:: bash

   # 1. Inspect restored files
   ls -la ~/.ssh

   # 2. Set directory to 700 and private keys to 600
   chmod 700 ~/.ssh
   chmod 600 ~/.ssh/id_* 2>/dev/null || true
   chmod 644 ~/.ssh/*.pub 2>/dev/null || true

   # 3. Ensure proper user ownership
   chown -R $USER:$USER ~/.ssh

----

Establishing Remote SSH Key Authentication
==========================================

To connect from another machine—such as your MacBook Pro (running macOS)—to
your Lenovo ThinkPad ``taylor`` (running Fedora 44) using SSH keys, you need
to configure network access, verify the SSH daemon, and copy your public
key.

Step 1: Find the IP Addresses
------------------------------

First, identify the local IP addresses of both systems.

On your Lenovo ThinkPad (Fedora Linux), open a terminal and run:

.. code-block:: bash

   hostname -I

*(Alternatively, use ``ip a`` and look for the ``inet`` address under your
Wi-Fi or Ethernet interface).*

On your MacBook Pro (macOS), open Terminal and run:

.. code-block:: bash

   ipconfig getifaddr en0

*(If connected via Wi-Fi, ``en0`` is typically your Wi-Fi interface).*

Step 2: Ensure SSH Server is Running on Fedora
----------------------------------------------

Before copying your key, ensure your ThinkPad allows incoming SSH
connections. On your ThinkPad, run:

.. code-block:: bash

   # Check if SSH daemon is active
   systemctl status sshd

   # If it is not active, start and enable it:
   sudo systemctl enable --now sshd

   # Ensure Fedora's firewall allows SSH traffic:
   sudo firewall-cmd --add-service=ssh --permanent
   sudo firewall-cmd --reload

Step 3: Copy Your Key from MacBook Pro to ThinkPad
--------------------------------------------------

Because your key file may have a custom name (such as
``porfirio@altair.pub`` instead of the default ``id_ed25519.pub``), you must
pass the ``-i`` flag to specify it.

Run this command from your MacBook Pro Terminal (replace ``username`` with
your Fedora username and ``192.168.1.50`` with your ThinkPad's IP):

.. code-block:: bash

   ssh-copy-id -i ~/.ssh/porfirio@altair.pub username@192.168.1.50

1. Confirm the connection prompt by typing ``yes`` and hitting Enter.
2. Enter your Fedora user password when prompted.
3. The key will be installed into ``~/.ssh/authorized_keys`` on your
   ThinkPad.

Step 4: Configure `~/.ssh/config` on Your MacBook Pro
-----------------------------------------------------

Since your key file has a custom name, macOS will not automatically use it
when running a standard SSH connection. To make connecting seamless, add
an entry to your ``~/.ssh/config`` file on your MacBook Pro:

1. Open the configuration file on your Mac:

   .. code-block:: bash

      nano ~/.ssh/config

2. Add the following host block:

   .. code-block:: text

      Host taylor
          HostName 192.168.1.50
          User username
          IdentityFile ~/.ssh/porfirio@altair

   *(Replace ``192.168.1.50`` with your ThinkPad's IP and ``username`` with
   your Fedora account name).*

3. Save and exit (`Ctrl + O`, `Enter`, then `Ctrl + X`).

Step 5: Test Passwordless SSH
-----------------------------

Now, from your MacBook Pro, you can connect passwordlessly by running:

.. code-block:: bash

   ssh taylor

----

Finishing Touches
=================

With these steps completed on Fedora 44, your SSH keys are safely backed
up, restored, and fully optimized for secure remote connections.
