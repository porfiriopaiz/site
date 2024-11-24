KeePassXC: The Password Manager
###############################

:date: 2017-11-17 19:10
:tags: debian, fc27, fedora, keepassxc, password
:category: floss
:slug: keepassxc-password-manager
:summary: A free and secure password manager.
:lang: en

KeePassXC is one of the first programs I install after booting a fresh system.

In this post, I’ll show you how to install KeePassXC on Fedora and Debian, how
to use it, how it simplifies managing hundreds of accounts and associated
passwords, and how to generate secure passwords with high entropy.

Installation
============

Fedora
------

.. code-block:: console

   su -c 'dnf install keepassxc'

Debian
------

.. code-block:: console

   su -c 'apt-get install keepassx'

Creating a Password Database
============================

The first step is to create your first database, where all generated passwords
for your accounts will be stored.

1. Launch KeePassXC:

   .. image:: {filename}/images/keepassxc/screenshot_from_2017-11-18_21-38-49.png
      :align: center
      :alt: Screenshot showing GNOME Shell overview mode and KeePassXC launcher

2. Create a new database:

   .. image:: {filename}/images/keepassxc/screenshot_from_2017-11-18_21-31-18.png
      :align: center
      :alt: KeePassXC interface with the option to create a new database

3. Assign a name to the `*.kdbx` file (the database):

   .. image:: {filename}/images/keepassxc/screenshot_from_2017-11-18_22-02-29.png
      :align: center
      :alt: Nautilus file explorer showing the new database file being saved

4. Set a master password to encrypt the database (`Passwords.kdbx`) and click `OK`:

   .. image:: {filename}/images/keepassxc/screenshot_from_2017-11-18_22-09-07.png
      :align: center
      :alt: KeePassXC while assigning the master password for the database

5. Add a new account and password by clicking the `Key` icon with a green arrow:

   .. image:: {filename}/images/keepassxc/screenshot_from_2017-11-20_16-37-51.png
      :align: center
      :alt: Button to add a new account to the database

6. Fill in the details:
   - Add a title to identify the account.
   - Specify the username for the account.

   .. image:: {filename}/images/keepassxc/screenshot_from_2017-11-19_22-15-14.png
      :align: center
      :alt: Adding a title, username, and password for a new account entry

7. Generate a secure password:
   - Click the black dice icon to open the password generator.
   - Adjust the character length for stronger passwords.
   - Select the character groups to include:

     - Uppercase letters: `A-Z`
     - Lowercase letters: `a-z`
     - Numbers: `0-9`
     - Special characters: `/*_ ...`
     - Extended ASCII characters (optional).

   - Enable:

     - **Exclude look-alike characters**
     - **Pick characters from every group**

   - Click `Generate` to create the password, then click `Copy` to copy it to the clipboard.

   .. image:: {filename}/images/keepassxc/screenshot_from_2017-11-19_22-17-30.png
      :align: center
      :alt: Random password generated based on selected criteria

8. Paste the generated password into the **Password** and **Repeat** fields using `Ctrl-v`:

   .. image:: {filename}/images/keepassxc/screenshot_from_2017-11-19_22-18-18.png
      :align: center
      :alt: Pasting the password into the required fields

9. Verify the password by clicking the `Eye` icon, then click `Apply` and `OK`.

   .. image:: {filename}/images/keepassxc/screenshot_from_2017-11-19_22-18-31.png
      :align: center
      :alt: Verifying passwords match in both fields

10. Save your changes by clicking the blue save icon. Confirm that the asterisk
(*) at the top disappears, indicating the changes have been saved.

   .. image:: {filename}/images/keepassxc/screenshot_from_2017-11-19_22-19-03.png
      :align: center
      :alt: Database changes successfully saved

Useful Keyboard Shortcuts
=========================

- **Ctrl-b**: Copy the username to the clipboard.
- **Ctrl-c**: Copy the password to the clipboard.
- **Ctrl-e**: Edit the selected account entry.
- **Ctrl-n**: Add a new account to the database.

Auto-Type Shortcut
==================

The **Auto-Type** shortcut, `Ctrl-v`, is my favorite. It allows KeePassXC to
enter the username and password for an account directly into the login fields
of a webpage or application.

For it to work, KeePassXC and the target field must be adjacent in the
task-switching order (`Alt-Tab`).

Example:
1. Select an entry with a URL:

   .. image:: {filename}/images/keepassxc/screenshot_from_2017-11-22_15-56-04.png
      :align: center
      :alt: Database entry with a linked URL

2. Press **Ctrl-u** to open the login page in your default web browser:

   .. image:: {filename}/images/keepassxc/screenshot_from_2017-11-22_16-35-24.png
      :align: center
      :alt: Opening the linked URL in a web browser

3. Switch back to KeePassXC using `Alt-Tab` and press `Ctrl-v` to enter the
username and password automatically:

   .. image:: {filename}/images/keepassxc/screenshot_from_2017-11-22_17-01-06.png
      :align: center
      :alt: Auto-Type entering the username and password

KeePassXC will then complete the login process for you.
