#!/bin/sh

#places the qn file in /usr/local/bin
destPath="/usr/local/bin"

sudo wget -O $destPath/qn https://raw.githubusercontent.com/vanCapelleRob/scripts/master/QuickNotes/qn
sudo chmod 755 $destPath/qn
sudo chown $USER:$USER $destPath/qn

mkdir /home/$USER/.quickNotes


#on manjaro, $USER changes to root, Ubuntu not.
#is_root(){
#	qnDir="/home/$1/.QuickNotes"
#	mkdir $qnDir
#	sudo chown $1:$1 $qnDir
#}

#is_user(){
#	qnDir="/home/$USER/.QuickNotes"
#	mkdir $qnDir
#	sudo chown $USER:$USER $qnDir
#}

#places the .help page in $HOME/.QuickNotes/.help
#if [ ! -z $1 ]; then
#	echo $USER
#	if [ $USER = 'root' ]; then
#		is_root $1
#	else
#		exit
 #		is_user
#	fi
#else
#	is_user
#fi

sudo wget -O $destPath/.help  https://raw.githubusercontent.com/vanCapelleRob/scripts/master/QuickNotes/help

#destroys the installation file
#rm qn_installer*
