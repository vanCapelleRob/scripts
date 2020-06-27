#!/bin/sh

#places the qn file in /usr/local/bin
destPath="/usr/local/bin"

sudo wget -O $destPath/qn https://raw.githubusercontent.com/vanCapelleRob/scripts/master/QuickNotes/qn
sudo chmod 755 $destPath/qn


#places the .help page in $HOME/.QuickNotes/.help
[ ! -z $1 ] && [ '$USER' = 'root' ] && qnDir="/home/$1/.QuickNotes" ; mkdir $qnDir ; sudo chown $1:$1 $qnDir || qnDir="/home/$USER/.QuickNotes" ; mkdir $qnDir ; sudo chown $USER:$USER $qnDir 


sudo wget -O $qnDir/.help  https://raw.githubusercontent.com/vanCapelleRob/scripts/master/QuickNotes/help

#destroys the installation file
rm qn_installer*
