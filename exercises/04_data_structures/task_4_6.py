# -*- coding: utf-8 -*-
"""
Task 4.6

Process the ospf_route string and print the information to the stdout as follows:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Restriction: All tasks must be done using the topics covered in this and previous chapters.

Warning: in section 4, the tests can be easily "tricked" into making the
correct output without getting results from initial data using Python.
This does not mean that the task was done correctly, it is just that at
this stage it is difficult otherwise test the result.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
prefix, AD, _, hop, last_update, outbound_interface = ospf_route.strip().split()
test = "test"
ospf_template = f'''
Prefix              {prefix:20}
AD/Metric           {AD:20}
Next-Hop            {hop:20}
Last Update         {last_update:20}
Outbound Interface  {outbound_interface:20}
'''
print(ospf_template)
