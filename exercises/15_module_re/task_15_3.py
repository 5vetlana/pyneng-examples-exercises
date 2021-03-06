# -*- coding: utf-8 -*-
"""
Task 15.3

Create a convert_ios_nat_to_asa function that converts NAT rules from
cisco IOS syntax to cisco ASA.

The function expects such arguments:
- the name of the file containing the Cisco IOS NAT rules
- the name of the file in which to write the NAT rules for the ASA

The function returns None.

Check the function on the cisco_nat_config.txt file.

Example cisco IOS NAT rules
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

And the corresponding NAT rules for the ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

In the file with the rules for the ASA:
- there should be no blank lines between the rules
- there must be no spaces before the lines "object network"
- there must be one space before the rest of the lines

In all rules for ASA, the interfaces will be the same (inside, outside).
"""
import re

def convert_ios_nat_to_asa(cisco_ios_file, asa_config_file):
    with open(cisco_ios_file) as input:
        with open(asa_config_file, 'w') as dest:
            search_line = r'ip nat inside source static tcp (?P<ip>[\d.]+)\s(?P<protocol>[\d]+) interface \S+ (?P<end>\d+)'
            regex = re.finditer(search_line,
                     input.read())
            for match in regex:
                asa_config_template = """
                object network {}
                host {}
                nat (inside, outside) static interface service tcp {} GigabitEthernet0/1 {}"""
                object_name = "LOCAL_" + match.group('ip')
                dest.write(asa_config_template.format(object_name, match.group('ip'), match.group('protocol'), match.group('end')))

convert_ios_nat_to_asa('cisco_nat_config.txt','asa_test1.txt')
