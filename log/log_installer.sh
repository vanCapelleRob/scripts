#!/bin/sh

#places the log file in /usr/local/bin
destPath="/usr/local/bin"

sudo wget -O $destPath/log https://raw.githubusercontent.com/vanCapelleRob/scripts/master/log/log
sudo chmod 755 $destPath/log


#places the .help page in $HOME/.logs/.help
mkdir $HOME/.logs
logDir="$HOME/.logs"
user=whoami
sudo chown $user:$user $logDir
sudo wget -O $logDir/.help  https://raw.githubusercontent.com/vanCapelleRob/scripts/master/log/help
