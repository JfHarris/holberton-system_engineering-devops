#!/usr/bin/bash
# Accepts a string as an argument, Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed, Ping the IP 5 times
if [ "$1" ]
then
    ping -c 5 "$1"
else
    echo "Usage: 5-is_the_host_on_the_network {IP_ADDRESS}"
fi
