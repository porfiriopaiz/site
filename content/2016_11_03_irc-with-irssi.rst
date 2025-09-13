IRC with irssi
##############

:date: 2016-11-3 21:20
:tags: cli, irc
:category: floss
:slug: irc-with-irssi
:summary:
:lang: en

Since my introduction to the realm of Free Software and GNU/Linux, one aspect
that has consistently captivated me is the formidable prowess of the command
line within this operating system. Whether it involves seamlessly navigating
through diverse directories or orchestrating the installation of an entire
operating system from the ground up, the terminal empowers users to
effortlessly accomplish a myriad of routine tasks.

.. TEASER_END

This post will guide you through configuring irssi to automate several
essential steps required to access a chat room. This includes connecting to the
server, authenticating, and seamlessly joining various channels of interest.

Installing irssi
================

To install irssi in fedora, just open a terminal and type the following
command:

.. code-block:: console

   su -c 'dnf install irssi'

And to install irssi in debian:

.. code-block:: console

   su -c 'apt-get install irssi'

Running irssi
-------------

Initiate irssi by opening a terminal and entering the following command:

.. code-block:: console

   irssi

Configurations
==============

Server Configurations
---------------------

All these commands must be executed within an irssi session.

To begin, let's remove the current server configuration we aim to automate.
Utilize the command ``/server list`` list to display the list of existing servers:

.. code-block:: console

   /server list

In our case, we will eliminate the current configuration for Freenode.

.. code-block:: console

   /server remove chat.freenode.net

Subsequently, incorporate the new configuration using the following command:

.. code-block:: console

   /SERVER ADD -auto -network Freenode chat.freenode.net 6667 your_nick_password

In this context, the ``-auto`` flag designates the connection to the
``Freenode`` server as automatic, while ``your_nick_password`` corresponds to
your user password.

Adding Channels
---------------

Likewise, you can append channels to this server to facilitate automatic
connection upon each login. To achieve this, execute the following command
within our irssi session:

.. code-block:: console

   /channel add -auto #fedora Freenode

Where ``-auto`` enables automatic joining to the ``#fedora`` channel at the
``Freenode`` server upon every login.

Concluding, after making any configuration adjustments, it is imperative to
save the changes using the command:

.. code-block:: console

   /save

Irssi automatically takes the username of your current system session as the
IRC user. To avoid discrepancies when your system username differs from your
Freenode user, run irssi with the following parameter:

.. code-block:: console

   irssi -n nick

Replace ``nick`` with your Freenode IRC username.

After successfully adding all your preferred channels from the Freenode server
and saving the modifications, simply execute the ``irssi`` command in a
terminal. You will be seamlessly connected to the server, and all the
designated channels will be accessible without the need for manual
authentication. This not only eliminates the risk of exposing your password
while typing but also streamlines the entire process—all from the convenience
of a terminal.
