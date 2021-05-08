#!/bin/bash

echo -e "Starting Basestation Setup\n"

usr=$(sudo whoami)
if [ $usr != "root" ]
then 
	>&2 echo -e "You do not have access to sudo."
	exit 1
fi

[ -d /etc/BESI-C ] || sudo mkdir /etc/BESI-C

if [ ! -d "/etc/BESI-C" ]
then 
	>&2 echo -e "Error creating BESI-C Path"
	exit 1
fi 

if [ -e "/etc/BESI-C/setup" ]
then
	echo "Setup has already been completed."
	exit 0
fi 

read -p "Basestation ID: " bs

if [ -z $bs ]
then 
	>&2 echo -e "Basestation invalid. Try again."
	exit 1
fi

#~~~~~~~~~~~~~~~~~~~~~~~~~~~ Hostname ~~~~~~~~~~~~~~~~~~~~~~~~~~~#
sudo cp /etc/hostname /etc/hostname.orig
echo -e $bs | sudo tee /etc/hostname > /dev/null

sudo cp /etc/hosts /etc/hosts.orig
echo -e "127.0.1.1\t$bs" | sudo tee -a /etc/hosts > /dev/null
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


echo -e "Setting up Basestation AP"

in_interface=wlan0
out_interface=wlan1

yes | sudo apt install dnsmasq hostapd

sudo systemctl stop dnsmasq
sudo systemctl stop hostapd

sudo mv /etc/dnsmasq.conf  /etc/dnsmasq.conf.orig

echo -e "interface=$interface\ndhcp-range=192.168.17.100,192.168.17.120,255.255.255.0,24h" | sudo tee -a /etc/dnsmasq.conf > /dev/null


sudo cp /etc/sysctl.conf /etc/sysctl.conf.orig
echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf > /dev/null

sudo sysctl -w net.ipv4.ip_forward=1

sudo iptables -t nat -A  POSTROUTING -o $in_interface -j MASQUERADE

sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"

sudo cp /etc/dhcpcd.conf /etc/dhcpcd.conf.orig
echo -e "interface $interface\n\tstatic ip_address=192.168.17.1/24\n\tnohook wpa_supplicant" | sudo tee -a /etc/dhcpcd.conf > /dev/null

(sudo cat /etc/rc.local | head -n -1  && echo -e "# call <periodictask>\n\niptables-restore < /etc/iptables.ipv4.nat\n\nexit0") > tmp

sudo cp /etc/rc.local /etc/rc.local.orig
cat tmp | sudo tee /etc/rc.local > /dev/null && rm tmp

echo -e "interface=$interface
driver=nl80211
ssid=BESI-Network
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=cancerpain
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP" | sudo tee /etc/hostapd/hostapd.conf > /dev/null

echo "DAEMON_CONF=\"/etc/hostapd/hostapd.conf\"" | sudo tee -a /etc/default/hostapd > /dev/null

sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd
sudo systemctl start dnsmasq
sudo systemctl reload dnsmasq
sudo service dhcpcd restart

echo -e "Basestation AP Setup Complete."


read -p  "Install Teamviewer? [y/n] " tv

if [ $tv = "y" ]
then 

echo -e "	Installing Teamviewer."

sudo wget https://dl.teamviewer.com/download/linux/version_15x/teamviewer-host_15.15.5_armhf.deb
yes | sudo apt install ./teamviewer-host_15.15.5_armhf.deb

echo -e "	Running Teamviewer as user" $(whoami)
echo -e "	Complete setup on Teamviewer window"
sudo -u pi teamviewer > /dev/null

fi

echo -e "Setup complete."

sudo touch /etc/BESI-C/setup > /dev/null

read -p "Reboot? [y/n] " re

if [ $re = "y" ]
then
	echo "Rebooting..."
	sudo reboot
	exit 0
fi

echo -e "Please reboot manually."
exit 0