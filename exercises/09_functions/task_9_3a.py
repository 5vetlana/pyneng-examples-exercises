# -*- coding: utf-8 -*-
"""
Task 9.3a

Make a copy of the code from the task 9.3.

Add this functionality: add support for configuration when the port is in VLAN 1
and the access port setting looks like this:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

In this case, information should be added to the dictionary that the port in VLAN 1
Dictionary example:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

The function must have one parameter, config_filename, which expects as an argument
the name of the configuration file.

Check the operation of the function using the config_sw2.txt file.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
def get_int_vlan_map(config_filename):
    """
    Takes a configuration file and returns a tuple of 2 dictionaries. The first dictionary is access interfaces and vlan values, the second dictionary is an interface and allowed vlans.

    * a dictionary of ports in access mode, where the keys are port numbers,
      and the access VLAN values (numbers):
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/16': 17}

    * a dictionary of ports in trunk mode, where the keys are port numbers,
      and the values are the list of allowed VLANs (list of numbers):
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}

    """
    with open(config_filename) as src:
        output = src.readlines()

    access_dict = {}
    trunk_dict = {}
    for line in output:
        if line.startswith("interface FastEthernet"):
            interface = line.split()[-1]
            access_dict[interface] = 1
        elif line.strip().startswith("switchport access vlan"):
            vlan = line.split()[-1]
            if vlan.isdigit():
                access_dict[interface] = vlan
        elif line.strip().startswith("switchport trunk allowed vlan"):
            vlan = line.split()[-1].split(',')
            trunk_dict[interface] = vlan
            del access_dict[interface]
    return (access_dict, trunk_dict)

print(get_int_vlan_map("config_sw2.txt"))
