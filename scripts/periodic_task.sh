#!/bin/bash

PATH="/home/pi/BESI-Digital_Relays/Data/"

cd $PATH

NAME="$(/usr/bin/uuid)"

/usr/bin/zip $NAME.zip *.csv
/usr/bin/python3 /home/pi/s3-uploader/upload.py $PATH $NAME.zip
