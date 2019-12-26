KeePassXC, the password manager
###############################

:date: 2017-11-17 19:10
:tags: debian, fc27, fedora, keepassxc, password
:category: floss
:slug: keepassxc-password-manager
:summary: A password manager Free and secure.
:lang: en

KeePassXC is one of the first programs that I install after the first boot of
any fresh install.

In the next post I will show how to install KeePassXC on Fedora and Debian, its
use and how it makes easier the management of hundreds of accounts and the
associated passwords, and how to generate secure passwords with the highest
levels of entropy.

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

Create a password database
==========================

The first thing we must do is create our first database in which we will keep
all the passwords that we generate for each account.

* Execute KeePassXC:

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-18_21-38-49.png
   :align: center

* Create a new database:

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-18_21-31-18.png
   :align: center

* Assign a name to the `*.kdbx` file, our database:

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-18_22-02-29.png
   :align: center

* It is time to assign a password, this will be the master password that We
  will use to decrypt the file `Passwords.kdbx`, we click on `OK`:

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-18_22-09-07.png
   :align: center

* To add a new account and its respective password, click on the icon of the
  `Key` with a green arrow:

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-20_16-37-51.png
   :align: center

* Add a title to identify what this password corresponds to, add the username
  to which the password We are going to create will belong:

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-19_22-15-14.png
   :align: center

* Then click on the black dots icon, notice how a new menu with options is
  displayed:

   - Click on the password tab, increase the amount of characters desired for
     our password, the more characters the higher the entropy level.

   - In the **Characters Types** section, We can select the different groups of
     characters We want to be present in our password:

      + Characters from `A` to `Z`, in capital letters: `A-Z`

      + Characters from `a` to `z`, in lower case: `a-z`

      + Numbers: `0-9`

      + Special characters: `/*_ ...`

      + Characters from `Extended ASCII <https://en.wikipedia.org/wiki/Extended_ASCII>`_

   - I marked them all.

      + With the mouse scroll go down and mark with a check:

         * **Exclude look alike characters**

         * **Pick characters from every group**

   - Finally click ``Generate`` to generate the password with the combination
     of selected characters and then ``Copy`` to copy the password to the
     clipboard.

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-19_22-17-30.png
   :align: center

* Now pressing `Ctrl-v` paste the password in the **Password** field and
  `Ctrl-V` in **Repeat**:

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-19_22-18-18.png
   :align: center

* By clicking on the `eye` icon we can reveal the password we have generated,
  copied and pasted in the **Password** and **Repeat** fields, click `Apply`
  and then `OK`:

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-19_22-18-31.png
   :align: center

* Note the asterisk in the upper border of the window at the end of
  `Passwords.kdbx`, this means that the changes have not been saved in the
  database:

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-19_22-18-58.png
   :align: center

* Click on the icon of the blue file to save the changes in the database:

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-22_16-21-04.png
   :align: center

* Note that the asterisk at the top edge of the screen at the end of
  `Passwords.kdbx` has disappeared, this means that the changes have already
  been saved in the database:

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-19_22-19-03.png
   :align: center

Useful keyboard shortcuts
=========================

**Ctrl** - **b** Copy the user to the clipboard.

**Ctrl** - **c** Copy the user's password to the clipboard.

**Ctrl** - **e** Open the menu to make modifications to the different accounts
that we have in our database.

**Ctrl** - **n** Allows you to add a new account to the database.

Self-writing shortcut
=====================

This keyboard shortcut is my favorite. It allows you to write the user and
password of an entry in our database directly to the page where that user and
password is used, so it is not necessary to use three shortcuts to achieve the
same result.

**Ctrl** - **v**

In order for it to work as it should, both KeePassXC and the field where the
user and password are introduced, must be a shot away from **Alt** - **Tab**.

By this I mean that if you press **Alt** - **Tab** you should move from the
``KeePassXC`` window to the browser window, for example:

Note that the account has a URL linked:

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-22_15-56-04.png
   :align: center

Go to our ``KeePassXC``, we select the entry of our database that corresponds
to the account in which we want to log in.

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-22_15-55-41.png
   :align: center

Press:

**Ctrl** - **u** to open the tab in which you will log in, this will open the
browser that we have configured as our default Web Browser, this page is
configured to locate the keyboard entry in the user field.

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-22_16-35-24.png
   :align: center

Press:

**Atl** - **Tab** to select the ``KeePassXC`` window back:

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-22_15-55-41.png
   :align: center

And then, making sure We still have selected the same entry in the database,
press:

**Ctrl** - **v**

.. image:: {filename}/images/keepassxc/screenshot_from_2017-11-22_17-01-06.png
   :align: center

The final result should make ``KeePassXC`` return to the browser, insert the
user, jump to the next field, insert the password, to finally and automatically
"press" ``Log In`` and log in.

I hope this post is useful for you.