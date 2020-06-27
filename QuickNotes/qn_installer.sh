#!/bin/sh

#places the qn file in /usr/local/bin
destPath="/usr/local/bin"

sudo wget -O $destPath/qn https://raw.githubusercontent.com/vanCapelleRob/scripts/master/QuickNotes/qn
sudo chmod 755 $destPath/qn


#places the .help page in $HOME/.QuickNotes/.help
qnDir="$HOME/.QuickNotes"
mkdir $qnDir && echo "made dir" || echo "didnt make dir"
sudo chown $USER:$USER $qnDir
sudo wget -O $qnDir/.help  https://raw.githubusercontent.com/vanCapelleRob/scripts/master/QuickNotes/help

#destroys the installation file
rm qn_installer*
