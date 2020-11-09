#!/bin/bash

# Installs Python Dependencies

yes | sudo apt-get install python3-pip 
sudo pip3 install --upgrade pip
sudo pip3 install --upgrade setuptools
sudo pip3 install RPI.GPIO
sudo pip3 install adafruit-circuitpython-tsl2591
sudo pip3 install adafruit-circuitpython-bme280
sudo pip3 install adafruit-io
sudo pip3 install -r packages.pk  