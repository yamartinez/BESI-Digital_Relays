#!/bin/bash

PATH="/home/pi/DeploymentData/"

cd $PATH

NAME="$(/usr/bin/uuid)"

/usr/bin/zip $NAME.zip *.csv
/usr/bin/python3 /home/pi/s3-uploader/upload.py $PATH $NAME.zip
