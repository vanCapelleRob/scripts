## QuickNotes
If you want to make notes of what you are doing on your system easy, this is
the program for you!

### How to install
run
> sudo wget -O /home/$USER/qn_installer https://raw.githubusercontent.com/vanCapelleRob/scripts/master/QuickNotes/qn_installer.sh && sudo chown $USER:$USER /home/$USER/qn_installer && sudo chmod 755 /home/$USER/qn_installer

> ./qn_installer in your home directory

I don't know why but on manjaro use (not yet tested)

> sudo sh qn_installer your_login_name


or

> sudo curl -LO https://raw.githubusercontent.com/vanCapelleRob/scripts/master/QuickNotes/qn_installer.sh && sudo chown $USER:$USER /home/$USER/qn_installer.sh && sudo chmod 755 /home/$USER/qn_installer.sh

> ./qn_installer.sh in your home directory

I don't know why but on manjaro use (not yet tested)

> sudo sh qn_installer.sh your_login_name

## What happens
A file /usr/bin/qn will be made. This file makes it all possible

A folder ~/.quickNotes will be created. This is where all your notes will be stored.

The qn_installer(.sh) will be deleted after installation.

## How it works
Simply type

> qn help

in a terminal and it will tell you how to work with it.

Basically, just typing

> qn myNote

will allow you to quicly write down what's on your mind, or what you need to remmember for later in a project.


## Be aware
If there is a new feature that might seem handy or makes the workflow better, you can always add it or contact me!
I will also update this page if i added something
