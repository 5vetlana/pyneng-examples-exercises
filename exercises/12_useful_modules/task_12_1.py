# -*- coding: utf-8 -*-
"""
Task 12.1

Create a ping_ip_addresses function that checks if IP addresses are pingable.

The function expects a list of IP addresses as an argument.

The function must return a tuple with two lists:
* list of available IP addresses
* list of unavailable IP addresses

To check the availability of an IP address, use the ping command.


Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
import subprocess

ip_addresses = ['8.8.8.8', '10.10.10.10', "8.8.4.4"]

def ping_ip_addresses(ip_address_list):
    """
    Ping IP address and return tuple:
        On success:
            * True, add to list of unavailable IP addresses
        On failure:
            * False, add to list of available IP address
    """
    available_ip = []
    unavailable_ip = []
    for ip_address in ip_address_list:
        reply = subprocess.run(['ping', '-n', '3', ip_address])

        if  reply.returncode == 0:
            unavailable_ip.append(ip_address)
        else:
            available_ip.append(ip_address)

    return (unavailable_ip, available_ip)

if __name__ == "__main__":
    print(ping_ip_addresses(ip_addresses))
