# -*- coding: utf-8 -*-
"""
Task 17.3

Create a function parse_sh_cdp_neighbors that processes the output of
the show cdp neighbors command.

The function expects, as an argument, the output of the command
as a single string (not a filename).
The function should return a dictionary that describes the connections between devices.

For example, if the following output was passed as an argument:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

The function should return a dictionary like this:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Interfaces must be written with a space. That is, so Fa 0/0, and not so Fa0/0.


Check the function on the contents of the sh_cdp_n_sw1.txt file
"""
import re

def parse_sh_cdp_neighbors(cdp_neigh_output):
    '''
    The function expects, as an argument, the output of the command
    as a single string (not a filename).
    The function should return a dictionary that describes the connections between devices.
    '''
    loc_device = re.search(r'(?P<local_device>\S+)>show cdp neighbors', cdp_neigh_output)
    local_device = loc_device.group('local_device')

    connections_dictionary = {}
    connections_dictionary[local_device] = {}
    regex = re.compile(r'(?P<rem_device>\S+)\s+(?P<local_intf>\S+ \d*/\d*).* (?P<rem_intf>\w+\s\d*/\d*)')
    for match in regex.finditer(cdp_neigh_output):
        rem_intf, rem_device, local_intf = match.group('rem_intf', 'rem_device', 'local_intf')
        connections_dictionary[local_device][local_intf] = {rem_device: rem_intf}
    return connections_dictionary

if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_sh_cdp_neighbors(f.read()))
