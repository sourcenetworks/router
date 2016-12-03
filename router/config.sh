# Configure a fresh Raspbian install
sudo apt-get update -y
sudo apt-get install dnsmasq hostapd -y

# Configure hostapd (configuration for access point)
echo "denyinterfaces wlan0" >> /etc/dhcpcd.conf
sudo cp interfaces /etc/network/interfaces
sudo service dhcpcd restart
sudo ifdown wlan0; sudo ifup wlan0

sudo cp hostapd.conf /etc/hostapd/hostapd.conf
sudo sed -i '/#DAEMON_CONF=""/c\DAEMON_CONF="/etc/hostapd/hostapd.conf"' \
  /etc/default/hostapd

# Configure dnsmasq (DHCP/DNS server)
sudo cp hostapd.conf /etc/hostapd/hostapd.conf

# Configure iptables
sudo iptables -F
sudo iptables -i wlan0 -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -i wlan0 -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -i wlan0 -A INPUT -p udp --dport 53 -j ACCEPT
sudo iptables -i wlan0 -A INPUT -p udp --dport 67:68 -j ACCEPT
sudo iptables -i wlan0 -A INPUT -j DROP
sudo sh -c "iptables-save > /etc/iptables.rules"

# Run
sudo service hostapd start
sudo service dnsmasq start
sudo reboot
