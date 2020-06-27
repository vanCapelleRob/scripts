#!/bin/sh

#places the log file in /usr/local/bin
destPath="/usr/local/bin"

sudo wget -O $destPath/log https://raw.githubusercontent.com/vanCapelleRob/scripts/master/log
sudo chmod 755 $destPath/log


#places the .help page in $HOME/.logs/.help
mkdir $HOME/.logs
logDir="$HOME/.logs"
sudo wget -O $logDir/.help  https://raw.githubusercontent.com/vanCapelleRob/scripts/master/help
