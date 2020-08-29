#!/bin/bash
sudo bash /home/pi/BESI-Digital_Relays/Beacon.sh
sudo python3 /home/pi/BESI-Digital_Relays/Sensors.py&>>/home/pi/Debug.log
#sudo python3 /home/pi/BESI-Digital_Relays/Sound.py &
