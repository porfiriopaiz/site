Backing Up an Android Device via MTP Using rsync on Fedora
##########################################################

:date: 2026-11-21 3:17
:tags: android, backup, cli, fedora, gvfs, mtp, rsync
:category: floss
:slug: rsync-android-mtp-gvfs-fedora
:summary: How to locate a GNOME GVfs MTP mount point and reliably back up
          files from an Android device to Linux using rsync without
          permission errors.
:lang: en

Standard ``rsync`` cannot directly read ``mtp://`` URLs because ``mtp://`` is
a **GVfs (GNOME Virtual File System)** abstraction rather than a POSIX
filesystem path. Since ``rsync`` requires direct access to a real filesystem
mount point, you must target the underlying directory where GNOME mounts MTP
devices inside ``/run/user/``.

----

Step 1: Locate the Local GVfs Mount Point
=========================================

Open a terminal on ``taylor`` and list the active GVfs mounts:

.. code-block:: bash

   ls -la /run/user/$UID/gvfs/

You will see a directory name starting with ``mtp:host=...``, corresponding
to your connected Android device (such as a Motorola ThinkPhone):

.. code-block:: text

   mtp:host=motorola_ThinkPhone_by_motorola_ZY22H4FF5S/

To access the internal storage directly, the full POSIX path on your
filesystem takes the following structure:

.. code-block:: bash

   /run/user/$UID/gvfs/mtp:host=motorola_ThinkPhone_by_motorola_ZY22H4FF5S/Internal shared storage

----

Step 2: Run rsync Against the GVfs Path
=======================================

Because MTP operates over a USB protocol that does not support Linux file
permission bits (``chmod``), file ownership (``chown``), or symbolic links,
running standard ``rsync -a`` (``--archive``) will trigger ``Operation not
permitted`` errors.

Instead, use the **`-rtvP`** flags (recursive, preserve times, verbose,
progress) and wrap the source path in double quotes to handle spaces and
special characters (``:``, ``=``):

.. code-block:: bash

   rsync -rtvP "/run/user/$UID/gvfs/mtp:host=motorola_ThinkPhone_by_motorola_ZY22H4FF5S/Internal shared storage/" /home/porfirio/antares/

.. note::
   Adding a trailing slash (``/``) at the end of ``"Internal shared
   storage/"`` copies the **contents** of your internal storage directly
   into ``/home/porfirio/antares/`` (e.g., ``DCIM``, ``Download``,
   ``Pictures``). If you omit the trailing slash on the source path, all
   contents will be placed inside a parent subdirectory named ``Internal
   shared storage``.

Flag Breakdown
--------------

- **`-r` (`--recursive`):** Recurses into all subdirectories (``DCIM``,
  ``Download``, ``Pictures``, etc.).
- **`-t` (`--times`):** Preserves original file modification timestamps.
- **`-v` (`--verbose`):** Displays files as they transfer.
- **`-P` (`--partial --progress`):** Displays a real-time progress bar for
  large transfers and retains partially transferred files so interrupted
  transfers can resume cleanly.

----

Step 3: Handling Connection Drops and MTP Timeouts
==================================================

MTP connections over USB can occasionally stall or drop during large file
transfers. If the process hangs or disconnects midway, simply re-run the
exact same ``rsync`` command.

Because timestamps are preserved via ``-t``, ``rsync`` will compare file
sizes and modification times, skip identical files that were already copied
completely, and resume right where it left off.
