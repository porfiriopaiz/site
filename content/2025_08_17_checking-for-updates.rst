Checking for updates
####################

:date: 2025-8-17 9:05
:tags: apple, cli, macOS
:category: misc
:slug: checking-for-updates
:summary: On macOS via command-line
:lang: en

In this post, we will explore the process of updating via the command-
line.

First thing to explore would be disabling the automatic updates process
on System Settings > General > Software Update > Automatic Updates > ⓘ.

Updates via command-line
========================

You can install macOS updates from the built-in command line using the
``softwareupdate`` utility in Terminal. This is often preferred by power
users and system administrators for its flexibility and ability to
automate tasks.

Here's a breakdown of how to do it:

**1. Open Terminal:**
You can find Terminal in ``Applications/Utilities`` or by searching for
it using Spotlight (Cmd + Space, then type "Terminal").

**2. Check for Available Updates:**
Before installing, it's good practice to see what updates are available
for your system. Use one of these commands:

.. code-block:: console

    softwareupdate -l

.. code-block:: console

    softwareupdate --list

This will list any pending updates, including macOS updates, Safari
updates, security updates, and other Apple software. You'll see
information like the update's name, version, and size. Look for items
marked ``[Recommended]`` and ``[restart]`` (indicating a restart is
needed).

**3. Install All Available Updates:**
To download and install all available updates, use the following command:

.. code-block:: console

    sudo softwareupdate -ia

.. code-block:: console

    sudo softwareupdate --install --all

- **``sudo``**: This grants administrative privileges, which are
  necessary for installing updates. You'll be prompted to enter your
  administrator password.
- **``-i`` or ``--install``**: This flag tells ``softwareupdate`` to
  install the updates.
- **``-a`` or ``--all``**: This flag tells ``softwareupdate`` to
  install all available updates.

**4. Install Specific Updates:**
If you only want to install a particular update from the list you saw
in step 2, you can specify its identifier:

.. code-block:: console

    sudo softwareupdate -i "Update Name-Version"

.. code-block:: console

    sudo softwareupdate --install "Update Name-Version"

**Important Notes:**
- The "Update Name-Version" is the exact identifier from the output of ``softwareupdate -l``.
- If the update name contains spaces, you **must** enclose it in single quotes (e.g., ``'macOS Ventura 13.5 Update-'``). Be precise with the name, including any trailing spaces if present in the output of ``-l``.

**5. Download Updates Without Installing:**
You can download updates to your system without immediately installing
them. This can be useful if you want to prepare updates for later
installation or for multiple machines.

.. code-block:: console

    sudo softwareupdate -d -a

.. code-block:: console

    sudo softwareupdate -d "Update Name-Version"

Downloaded updates are usually stored in ``/Library/Updates``. You can
then install them later using the ``-i`` or ``--install`` command.

**6. Restart After Installation:**
Many macOS updates require a restart to complete the installation. The
``softwareupdate`` command will usually prompt you to restart or handle
it automatically if you use the ``-R`` flag.

.. code-block:: console

    sudo softwareupdate -iaR

It's generally a good idea to perform the restart when prompted or
manually after the installation is complete.

Important Considerations
========================

- **Backup Your Mac:** Before performing any major system update, it's
  always highly recommended to back up your Mac using Time Machine or
  another backup solution.
- **Administrator Password:** You will need your administrator
  password to use ``sudo`` and install updates.
- **Internet Connection:** A stable internet connection is essential
  for downloading updates.
- **Disk Space:** Ensure you have enough free disk space for the
  updates.
- **Third-Party Apps:** The ``softwareupdate`` command handles Apple
  system updates and built-in Apple apps. It does not update
  third-party apps from the Mac App Store or other sources.
- **Command Line Tools for Xcode:** If you develop or use certain
  development tools, you might also need to update the Xcode Command
  Line Tools. You can usually do this with ``xcode-select --install``
  or through ``softwareupdate``.

By using the ``softwareupdate`` command, you gain more control over when
and how your macOS updates are applied, which can be particularly
useful in automated environments or for troubleshooting.
