#!/bin/bash

PATH="/home/pi/BESI-Digital_Relays/Data/"

cd $PATH

NAME="$(/usr/bin/uuid)"

/usr/bin/zip $NAME.zip *.csv
/usr/bin/python3 /home/pi/s3-uploader/upload.py $PATH $NAME.zip


# Testing git pull and reboot - will move this to a daily thing at like 2am
cd ..
git pull 
reboot