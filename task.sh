#!/bin/bash

PATH="/home/pi/DeploymentData"

/bin/mkdir $PATH/tmp

/bin/mv $PATH/Humidity/* $PATH/tmp
/bin/mv $PATH/Temperature/* $PATH/tmp
/bin/mv $PATH/Sound/* $PATH/tmp
/bin/mv $PATH/Pressure/* $PATH/tmp
/bin/mv $PATH/Light/* $PATH/tmp

NAME="$(/usr/bin/uuid)"

/usr/bin/zip $PATH/$NAME.zip $PATH/tmp/*

/bin/rm -r $PATH/tmp
