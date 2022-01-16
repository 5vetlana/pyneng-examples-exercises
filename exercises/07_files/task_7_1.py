# -*- coding: utf-8 -*-
"""
Task 7.1

Process the lines from the ospf.txt file and print information for each line
in this form to the stdout:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
with open("ospf.txt") as f:
    output = f.readlines()

ospf_template ='''
Prefix              {}
AD/Metric           {}
Next-Hop            {}
Last update         {}
Outbound Interface  {}
'''

for line in output:
    line = line.replace(',',' ').split()
    prefix = line[1]
    AD = line[2]
    Next_Hop = line[4]
    Last_update = line[5]
    Outbound_int = line[6]
    print(ospf_template.format(prefix, AD, Next_Hop, Last_update, Outbound_int))
