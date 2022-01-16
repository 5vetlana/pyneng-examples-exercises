# -*- coding: utf-8 -*-
"""
Task 6.1

The mac list contains MAC addresses in the format XXXX:XXXX:XXXX
However, in Cisco equipment MAC addresses are in XXXX.XXXX.XXXX format.

Write a code that converts MAC addresses to cisco format and adds them to
a new list named result.
Print the result list to the stdout using print.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]

new_mac = []
for address in mac:
    cisco_format = address.replace(":", ".")
    new_mac.append(cisco_format)

print(new_mac)
