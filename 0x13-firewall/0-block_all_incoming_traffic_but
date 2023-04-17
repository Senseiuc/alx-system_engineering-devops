#!/usr/bin/bash
# a file that installs and sets up firewall
sudo apt install ufw
sudo sed -i 's/IPV6=no/IPV6=yes/g' /etc/default/ufw
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
sudo ufw disable
sudo ufw --force enable
