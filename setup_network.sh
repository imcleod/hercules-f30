#!/bin/bash

iptables -t nat -A POSTROUTING -s 192.168.200.0/24 -d 0.0.0.0/0 -j MASQUERADE
echo 1 > /proc/sys/net/ipv4/ip_forward
