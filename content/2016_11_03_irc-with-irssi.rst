IRC with irssi
##############

:date: 2016-11-3 21:20
:tags: cli, irc
:category: floss
:slug: irc-with-irssi
:summary:
:lang: en

From my beginnings in the Free Software and GNU/Linux, one of the features
that caught my attention is the power of the command line in this operating
system. From moving between different directories or installing an operating
system completely from scratch, these are some of the routine tasks you can
achive from the terminal.

.. TEASER_END

In this post I will show how to configure irssi to automate some of the steps to
carry out in order to access a chat room, as it is connecting to the server,
authenticate and then joining the differents channels that are of interest.

Installing irssi
================

To install irssi in fedora, just open a terminal and type the following command:

.. code-block:: console

    su -c 'dnf install irssi'

And to install irssi in debian:

.. code-block:: console

    su -c 'apt-get install irssi'

Running irssi
-------------

To run irssi, open a terminal and type the following command:

.. code-block:: console

    irssi

Configurations
==============

Server Configurations
---------------------

All these commands must be executed on a irssi session.

First we will remove the existing server configuration that we want to automate.
With ``/server list`` we can view existing servers:

.. code-block:: console

    /server list

In our case we will remove the existing configuration of Freenode.

.. code-block:: console

    /server remove chat.freenode.net

And add the new configuration with the following command:

.. code-block:: console

    /SERVER ADD -auto -network Freenode chat.freenode.net 6667 your_nick_password

In which ``-auto`` defines the connection to the ``Freenode`` server as
automatic and ``your_nick_password`` is your user password.

Adding Channels
---------------
Similarly, it is possible to add channels to this server in order to get
connected automatically on each login, for this run the following command in our
irssi session:

.. code-block:: console

    /channel add -auto #fedora Freenode

In which ``-auto`` allows us joining to ``#fedora`` channel at ``Freenode``
server automatically at each login.

Finally, every time we make a change in our configuration, we must save changes
with the command:


.. code-block:: console

    /save

irssi takes the user name of your current session on the system as the user for
your session in irc, to prevent this from happening if the name of your session
in the system does not match your user at Freenode, you should run irssi with
the following parameter:

.. code-block:: console

    irssi -n nick

Where ``nick`` is your user nick on Freenode IRC.

Once you've added all your channels of interest from the Freenode server and
saved the changes, you only need to run in a terminal the ``irssi`` command and
automatically you will be connected to the server and all the channels you've
added without needing to authenticate manually and without risking anyone from
reading your password while you type it. All this from a terminal.
