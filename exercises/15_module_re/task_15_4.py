# -*- coding: utf-8 -*-
"""
Task 15.4

Create a get_ints_without_description function that expects as an argument
the name of the file containing the device configuration.

The function should process the configuration and return a list of interface names,
which do not have a description (description command).

An example of an interface with a description:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Interface without description:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Check the operation of the function using the example of the config_r1.txt file.
"""
import re

def get_ints_without_description(device_config_file):
    with open(device_config_file) as src:
        regex = re.compile(r'interface (?P<intf>\S+\d+)\n'
                           r'(?P<desc> description .*)*')
        intf_list = []
        for match in regex.finditer(src.read()):
            if not match.group('desc'):
                intf_list.append(match.group('intf'))
        return intf_list

print(get_ints_without_description('config_r1.txt'))
