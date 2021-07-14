#!/bin/bash

if [ ! -e "/etc/BESI-C/setup" ]
then
	echo "Setup has not been completed"
	exit 0
fi 

echo -e "Starting Basestation Teardown\n"

usr=$(sudo whoami)
if [ $usr != "root" ]
then 
	>&2 echo -e "You do not have access to sudo."
	exit 1
fi

read -p "Are you sure you want to revert configurations to default? [y/n] " re
if [ $re = "y" ]
then

    # Revert Files to Original State
    sudo mv /etc/hostname.orig /etc/hostname 
    sudo mv /etc/hosts.orig /etc/hosts 
    sudo mv /etc/dnsmasq.conf.orig /etc/dnsmasq.conf  
    sudo mv /etc/sysctl.conf.orig /etc/sysctl.conf 
    sudo mv /etc/dhcpcd.conf.orig /etc/dhcpcd.conf 
    sudo mv /etc/rc.local.orig /etc/rc.local 

    sudo rm /etc/BESI-C/setup

    echo "Settings have been reverted."

    read -p "Reboot now? [y/n] " re

    if [ $re = "y" ]
    then
        echo "Rebooting..."
        sudo reboot
        exit 0
    fi

else 
	echo "Cancelling... "
	exit 0
fi

exit 0