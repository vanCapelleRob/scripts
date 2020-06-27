#!/bin/sh

#places the qn file in /usr/local/bin
destPath="/usr/local/bin"

sudo wget -O $destPath/qn https://raw.githubusercontent.com/vanCapelleRob/scripts/master/QuickNotes/qn
sudo chmod 755 $destPath/qn


#places the .help page in $HOME/.QuickNotes/.help
mkdir $HOME/.QuickNotes
logDir="$HOME/.QuickNotes"
sudo chown $USER:$USER $logDir
sudo wget -O $logDir/.help  https://raw.githubusercontent.com/vanCapelleRob/scripts/master/QuickNotes/help

#destroys the installation file
rm qn_installer*
