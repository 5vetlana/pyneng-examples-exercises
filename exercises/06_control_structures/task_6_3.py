# -*- coding: utf-8 -*-
"""
Task 6.3

A configuration generator for access ports is made in the script.
Make a similar configuration generator for trunk ports.

In trunks, the situation is complicated by the fact that there can be many VLANs,
and you need to understand what to do with them (add, delete, overwrite).

Therefore, in accordance with each port there is a list and the first (zero index)
element of the list specifies how to interpret VLAN numbers that follow.


Dict value and corresponding command:
* ['add', '10', '20'] - switchport trunk allowed vlan add 10,20
* ['del', '17'] - switchport trunk allowed vlan remove 17
* ['only', '11', '30'] - switchport trunk allowed vlan 11,30

Task for ports 0/1, 0/2, 0/4:
- generate a configuration based on the trunk_template template
- taking into account the keywords add, del, only

The code should not be tied to specific port numbers. I.e,
if there are other interface numbers in the trunk dictionary, the code should work.

For data in the trunk_template dictionary, output to
the standard output should be like this:
interface FastEthernet 0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan add 10,20
interface FastEthernet 0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 11,30
interface FastEthernet 0/4
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan remove 17

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

for intf, vlan in access.items():
    print("interface FastEthernet" + intf)
    for command in access_template:
        if command.endswith("access vlan"):
            print(f" {command} {vlan}")
        else:
            print(f" {command}")

for intf, vlan in trunk.items():
    print("interface FastEthernet" + intf)
    for command in trunk_template:
        vlans = ",".join(trunk[intf][1:])
        if command.endswith("allowed vlan"):
            if vlan[0] == "add":
                print(f"{command} add {vlans}")
            elif vlan[0] == "only":
                print(f"{command} {vlans}")
            elif vlan[0] == "del":
                print(f'{command} remove {vlans}')
        else:
            print(f"{command}")
