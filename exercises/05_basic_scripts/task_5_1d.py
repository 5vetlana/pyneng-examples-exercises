# -*- coding: utf-8 -*-
"""
Task 5.1d

Modify the script from task 5.1c so that, when requesting a parameter,
the user could enter the parameter name in any case.

An example of script execution:
$ python task_5_1d.py
Enter device name: r1
Enter parameter name (ios, model, vendor, location, ip): IOS
15.4


Restriction: You cannot modify the london_co dictionary.

All tasks must be completed using only the topics covered. That is, this task can be
solved without using the if condition.
"""

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

#List all devices currently in list
all_devices = ",".join(london_co.keys())
device = input(f"Enter device name ({all_devices}): ").lower()
#list all parameters for a specified device
parameters = ",".join(london_co[device].keys())
print(parameters)
param = input(f"Enter parameter name ({parameters}): ").lower()
#Print parameter for chosen device
print(london_co[device].get(param, "There is no such parameter"))
