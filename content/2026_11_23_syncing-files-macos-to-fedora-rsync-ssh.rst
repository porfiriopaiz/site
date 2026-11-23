Syncing Files from macOS to Fedora Linux with rsync and SSH
###########################################################

:date: 2026-11-23 6:01
:tags: backup, cli, fedora, linux, macos, rsync, ssh, zsh
:category: floss
:slug: syncing-files-macos-to-fedora-rsync-ssh
:summary: A complete guide on configuring rsync workflows from macOS to
          Fedora Linux over SSH, covering short vs. long flags, global
          exclusion lists, shell aliases, and SSH host key troubleshooting.
:lang: en

When transferring files between a macOS workstation (such as my MacBook Air
``ankaa``) and a Fedora Linux machine (my Lenovo ThinkPad T450 ``taylor``),
``rsync`` over SSH provides fast, incremental synchronization. Once the
``taylor`` host alias is configured in ``~/.ssh/config``, ``rsync``
automatically inherits your target IP address (``192.168.0.10``), username,
and custom identity key without requiring explicit connection flags on every
run.

----

The Recommended Command Structure (Short Flags)
===============================================

The standard pattern for copying files from macOS to a remote Linux host
uses compact short options:

.. code-block:: bash

   rsync -avzP /path/to/local/source/ taylor:/path/to/remote/destination/

Flag Breakdown (``-avzP``)
--------------------------

- **`-a` (archive mode):** Preserves file permissions, ownership,
  timestamps, and symbolic links recursively.
- **`-v` (verbose):** Displays which files are being transferred.
- **`-z` (compress):** Compresses data in transit to speed up transfers
  over Wi-Fi or LAN.
- **`-P` (progress and partial):** Displays real-time progress bars and
  retains partially transferred files to allow resuming interrupted
  transfers.

Common Use Cases and Trailing Slashes
-------------------------------------

1. **Transferring a Single File:**

   .. code-block:: bash

      rsync -avzP ~/Downloads/document.pdf taylor:~/Downloads/

2. **Transferring an Entire Folder:**

   Pay close attention to the trailing slash (``/``) on the source directory:

   - **Copy the contents of a directory into a target folder** (note the
     trailing slash on ``Photos/``):

     .. code-block:: bash

        rsync -avzP ~/Photos/ taylor:~/Pictures/

     *(Result: Files inside ``~/Photos/`` are placed directly inside
     ``~/Pictures/`` on ``taylor``).*

   - **Copy the directory itself as a subdirectory** (no trailing slash on
     ``Photos``):

     .. code-block:: bash

        rsync -avzP ~/Photos taylor:~/Pictures/

     *(Result: Creates ``~/Pictures/Photos/`` on ``taylor``).*

Safe Verification: Run a Dry Run First (``-n``)
-----------------------------------------------

To preview which files will be copied or updated without modifying anything
on disk, pass the ``-n`` (or ``--dry-run``) flag:

.. code-block:: bash

   rsync -avzPn ~/Documents/ taylor:~/Documents/

Once you confirm the file list looks accurate, remove the ``n`` flag to
perform the live transfer.

----

Short Flags vs. Long Options
============================

Short options (like ``-a``, ``-v``, ``-z``) are single-letter abbreviations
designed for quick terminal input. Long options (like ``--archive``,
``--verbose``, ``--compress``) perform the exact same operations while
remaining self-documenting and easier to read in scripts and documentation.

+------------+------------------------+-----------------------------------------------+
| Short Flag | Equivalent Long Option | What It Does                                  |
+============+========================+===============================================+
| ``-a``     | ``--archive``          | Enables recursion and preserves permissions,  |
|            |                        | modification times, ownership, and symlinks.  |
+------------+------------------------+-----------------------------------------------+
| ``-v``     | ``--verbose``          | Displays detailed information about which     |
|            |                        | files are being transferred.                  |
+------------+------------------------+-----------------------------------------------+
| ``-z``     | ``--compress``         | Compresses file data during network transit   |
|            |                        | to speed up transfer times over Wi-Fi.        |
+------------+------------------------+-----------------------------------------------+
| ``-P``     | ``--progress``         | Combined shortcut: ``--progress`` shows the   |
|            | ``--partial``          | live bar; ``--partial`` keeps incomplete      |
|            |                        | files if the connection breaks for resuming.  |
+------------+------------------------+-----------------------------------------------+
| ``-n``     | ``--dry-run``          | Performs a trial run showing what would       |
|            |                        | change without transferring or modifying      |
|            |                        | any files.                                    |
+------------+------------------------+-----------------------------------------------+
| ``-u``     | ``--update``           | Skips files that are already newer on the     |
|            |                        | destination host (``taylor``).                |
+------------+------------------------+-----------------------------------------------+

What ``--update`` Adds to Your Workflow
---------------------------------------

Adding ``--update`` instructs ``rsync`` to compare file timestamps across
both machines:

- If a file on ``taylor`` is **newer** than the corresponding file on your
  Mac, ``rsync`` will **not** overwrite it.
- This prevents accidentally rolling back recent edits made directly on the
  remote Linux workstation.

Recommended Command Structure (Long Options)
--------------------------------------------

Using explicit long options, the standard transfer syntax becomes:

.. code-block:: bash

   rsync --archive --verbose --update --compress --progress --partial /path/to/local/source/ taylor:/path/to/remote/destination/

.. note::
   ``--compress`` is optional over fast local networks, though still
   recommended when transferring large text files, source code repositories,
   or scripts.

Long-Option Use Cases and Dry Runs
----------------------------------

1. **Transferring a Single File:**

   .. code-block:: bash

      rsync --archive --verbose --update --progress --partial ~/Downloads/document.pdf taylor:~/Downloads/

2. **Transferring Directory Contents vs. Subdirectories:**

   - **Copy contents directly** (trailing slash on ``Photos/``):

     .. code-block:: bash

        rsync --archive --verbose --update --compress --progress --partial ~/Photos/ taylor:~/Pictures/

   - **Copy the directory itself** (no trailing slash on ``Photos``):

     .. code-block:: bash

        rsync --archive --verbose --update --compress --progress --partial ~/Photos taylor:~/Pictures/

3. **Running a Dry Run with Long Options:**

   .. code-block:: bash

      rsync --dry-run --archive --verbose --update --progress --partial ~/Documents/ taylor:~/Documents/

----

Filtering macOS Metadata Files
==============================

macOS automatically generates hidden metadata files such as ``.DS_Store``
and ``.localized`` that clutter Linux directories. You can exclude them
per command or configure a permanent global exclusion list.

Option 1: Inline Exclusions (Per-Command)
-----------------------------------------

Pass individual ``--exclude`` parameters directly to ``rsync``:

.. code-block:: bash

   rsync --archive --verbose --update --progress --partial \
     --exclude='.DS_Store' \
     --exclude='.localized' \
     --exclude='._*' \
     --exclude='.CFUserTextEncoding' \
     ~/Desktop/ taylor:~/Desktop/

Common macOS metadata files to exclude include:

- ``.DS_Store`` (Finder folder display settings)
- ``.localized`` (system folder localization hints)
- ``._*`` (AppleDouble resource fork files created on non-HFS/APFS
  volumes)
- ``.CFUserTextEncoding`` (user text encoding preferences)
- ``.Trashes`` and ``.Spotlight-V100`` (system trash and Spotlight index
  directories)

One-Liner with Zsh Brace Expansion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because macOS uses ``zsh`` as its default shell, you can collapse multiple
``--exclude`` flags into a single brace expansion one-liner:

.. code-block:: bash

   rsync --archive --verbose --update --progress --partial --exclude={'.DS_Store','.localized','._*','.CFUserTextEncoding'} ~/Desktop/ taylor:~/Desktop/

The shell expands ``{...}`` into separate ``--exclude`` arguments before
executing ``rsync``.

Option 2: Permanent Global Exclusion List (Recommended)
-------------------------------------------------------

To avoid typing exclusion flags repeatedly, define a global ignore file in
your home directory and alias ``rsync`` in ``~/.zshrc``.

1. **Create ``~/.rsync-exclude`` on macOS:**

   .. code-block:: bash

      cat << 'EOF' > ~/.rsync-exclude
      .DS_Store
      .localized
      ._*
      .CFUserTextEncoding
      .Trashes
      .Spotlight-V100
      EOF

2. **Add an alias to ``~/.zshrc``:**

   Open ``~/.zshrc`` in your editor:

   .. code-block:: bash

      nano ~/.zshrc

   Append the following line and save the file:

   .. code-block:: bash

      alias rsync='rsync --exclude-from="$HOME/.rsync-exclude"'

   Reload your shell configuration:

   .. code-block:: bash

      source ~/.zshrc

3. **Run your standard sync command:**

   .. code-block:: bash

      rsync --archive --verbose --update --progress --partial ~/Desktop/ taylor:~/Desktop/

Cleaning Up Existing Metadata Files on Linux
--------------------------------------------

If macOS metadata files were already synced to ``taylor`` previously, you
can remove them remotely via SSH:

.. code-block:: bash

   ssh taylor "find ~/Desktop -name '.DS_Store' -o -name '.localized' -delete"

----

SSH Host Key Troubleshooting and Connection Verification
========================================================

When reinstalling Fedora Linux on ``taylor`` while retaining the same local
IP address (``192.168.0.10``), SSH generates a new host key fingerprint.
Attempting to copy keys or connect from ``ankaa`` will trigger a remote host
identification warning because the stored fingerprint in
``~/.ssh/known_hosts`` no longer matches.

Step 1: Remove the Stale Host Key Entry
---------------------------------------

Clear the old fingerprint for ``192.168.0.10`` from ``ankaa``:

.. code-block:: bash

   ssh-keygen -R 192.168.0.10

This removes the outdated entry from ``~/.ssh/known_hosts`` and saves a
backup copy of the previous file.

Step 2: Copy Your Public Key and Accept the New Fingerprint
-----------------------------------------------------------

Re-run ``ssh-copy-id`` using your custom-named public key:

.. code-block:: bash

   ssh-copy-id -i ~/.ssh/porfirio@ankaa.pub porfirio@192.168.0.10

Type ``yes`` when prompted to trust the new host fingerprint, then enter
your Fedora password to install the public key on ``taylor``.

Step 3: Configure ``~/.ssh/config`` and Test Connections
--------------------------------------------------------

Ensure your SSH client configuration on ``ankaa`` points to the private key
file (without the ``.pub`` extension):

.. code-block:: bash

   nano ~/.ssh/config

.. code-block:: text

   Host taylor
       HostName 192.168.0.10
       User porfirio
       IdentityFile ~/.ssh/porfirio@ankaa

Enforce strict permissions on the configuration file:

.. code-block:: bash

   chmod 600 ~/.ssh/config

You can now verify passwordless authentication using three methods:

1. **Direct connection with explicit identity flag:**

   .. code-block:: bash

      ssh -i ~/.ssh/porfirio@ankaa porfirio@192.168.0.10

2. **Non-interactive remote command execution:**

   .. code-block:: bash

      ssh -i ~/.ssh/porfirio@ankaa porfirio@192.168.0.10 "hostname; uptime"

3. **Alias-based connection:**

   .. code-block:: bash

      ssh taylor

If SSH still prompts for a password, run the connection in verbose mode
(``-v``) to inspect key negotiation:

.. code-block:: bash

   ssh -v -i ~/.ssh/porfirio@ankaa porfirio@192.168.0.10
