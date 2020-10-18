#!/bin/sh

destPath="/usr/local/bin"

sudo wget -O $destPath/tasks https://raw.githubusercontent.com/vanCapelleRob/scripts/master/tasksHelper/tasks
&& sudo mkdir $destPath/.tasksCode

&& sudo chmod 755 $destPath/tasks 
&& sudo chown $USER:$USER $destPath/tasks 
# && sudo chmod 755 $destPath/.tasksCode
&& sudo chown $USER:$USER $destPath/.tasksCode

&& sudo wget -O $destPath/.tasksCode/App.py
&& sudo wget -O $destPath/.tasksCode/main.py
&& sudo wget -O $destPath/.tasksCode/Task.py

&& sudo chmod 755 $destPath/.tasksCode/*
&& sudo chown $USER:$USER $destPath/.tasksCode/*

&& mkdir /home/$USER/.tasks
&& sudo wget -O $destPath/.help_tasksHelper  link to help file 
&& rm /home/$USER/tasksHelper_installer*
