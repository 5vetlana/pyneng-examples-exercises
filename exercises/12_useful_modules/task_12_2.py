# -*- coding: utf-8 -*-
"""
Task 12.2

The ping_ip_addresses function from task 12.1 only accepts a list of addresses,
but it would be convenient to be able to specify addresses using a range,
for example 192.168.100.1-10.

In this task, you need to create a function convert_ranges_to_ip_list that
converts a list of IP addresses in different formats into a list where each
IP address is listed separately.

The function expects as an argument a list containing IP addresses
and/or ranges of IP addresses.

List items can be in the format:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

If the address is specified as a range, the range must be expanded into
individual addresses, including the last address in the range.
To simplify the task, we can assume that only the last octet of the
address changes in the range.

The function returns a list of IP addresses.

For example, if you pass the following list to the convert_ranges_to_ip_list function:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

The function should return a list like this:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress

addresses = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

def convert_ranges_to_ip_list(ip_addresses):
    ip_address_list = []
    for ip_address in ip_addresses:
        if '-' in ip_address:
            first_ip, last_ip = ip_address.split('-')
            if '.' not in last_ip:
                compiled_ip = '.'.join(first_ip.split('.')[:3]) + '.' + last_ip
                first_ip = ipaddress.ip_address(first_ip)
                last_ip = ipaddress.ip_address(compiled_ip)
                for ip in range(int(first_ip), int(last_ip) + 1):
                    ip_address_list.append(str(ipaddress.ip_address(ip)))
            else:
                first_ip = ipaddress.ip_address(first_ip)
                last_ip = ipaddress.ip_address(last_ip)
                for ip in range(int(first_ip), int(last_ip) + 1):
                    ip_address_list.append(str(ipaddress.ip_address(ip)))
        else:
            ip_address_list.append(ip_address)
    return ip_address_list

if __name__ == "__main__":
    print(convert_ranges_to_ip_list(addresses))
