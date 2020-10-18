#!/bin/sh

destPath="/usr/local/bin"

sudo wget -O $destPath/tasks https://raw.githubusercontent.com/vanCapelleRob/scripts/master/tasksHelper/tasks
sudo mkdir $destPath/.tasksCode

sudo chmod 755 $destPath/tasks 
sudo chown $USER:$USER $destPath/tasks 
# sudo chmod 755 $destPath/.tasksCode
sudo chown $USER:$USER $destPath/.tasksCode

sudo wget -O $destPath/.tasksCode/App.py https://raw.githubusercontent.com/vanCapelleRob/scripts/master/tasksHelper/pyCode/App.py
sudo wget -O $destPath/.tasksCode/main.py https://raw.githubusercontent.com/vanCapelleRob/scripts/master/tasksHelper/pyCode/main.py
sudo wget -O $destPath/.tasksCode/Task.py https://raw.githubusercontent.com/vanCapelleRob/scripts/master/tasksHelper/pyCode/Task.py

sudo chmod 755 $destPath/.tasksCode/*
sudo chown $USER:$USER $destPath/.tasksCode/*

mkdir /home/$USER/.tasks
sudo wget -O $destPath/.help_tasksHelper  link to help file 
rm /home/$USER/tasksHelper_installer*
