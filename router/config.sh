## This file will run the commands to set up an out of box rpi3 to run
## source

# Configure IP tables
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to 9090

# Configure NAT
