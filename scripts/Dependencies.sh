#!/bin/bash

# Installs Python Dependencies

yes | sudo apt-get install python3-pip 
sudo pip3 install --upgrade pip
sudo pip3 install --upgrade setuptools
yes | sudo apt-get install libjack-jackd2-dev portaudio19-dev
sudo pip3 install -r requirements.txt
