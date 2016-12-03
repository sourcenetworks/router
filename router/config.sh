# Configure a fresh Raspbian install
sudo apt-get update -y
sudo apt-get install dnsmasq hostapd -y

# Configure hostapd (configuration for access point)
sudo cp interfaces /etc/network/interfaces
sudo cp hostapd.conf /etc/hostapd/hostapd.conf
sudo sed -i "/DAEMON_CONF=/c\DAEMON_CONF=/etc/hostapd/hostapd.conf" \
  /etc/init.d/hostapd

# Configure dnsmasq (DHCP/DNS server)
sudo cp dnsmasq.conf /etc/dnsmasq.conf

# Configure iptables
sudo iptables -F
sudo iptables -i wlan0 -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -i wlan0 -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -i wlan0 -A INPUT -p udp --dport 53 -j ACCEPT
sudo iptables -i wlan0 -A INPUT -p udp --dport 67:68 -j ACCEPT
sudo iptables -i wlan0 -A INPUT -j DROP
sudo sh -c "iptables-save > /etc/iptables.rules"

# Run
sudo update-rc.d hostapd defaults
sudo update-rc.d dnsmasq defaults
sudo reboot
