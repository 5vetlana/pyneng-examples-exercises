# -*- coding: utf-8 -*-
"""
Task 4.7

Convert MAC address in mac string to binary string like this:
'101010101010101010111011101110111100110011001100'

Print the resulting new string to the standard output (stdout) using print.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

Warning: in section 4, the tests can be easily "tricked" into making the
correct output without getting results from initial data using Python.
This does not mean that the task was done correctly, it is just that at
this stage it is difficult otherwise test the result.
"""

mac = "AAAA:BBBB:CCCC"
mac = mac.split(":")
mac = ''.join(mac)
mac1, mac2, mac3, mac4, mac5, mac6 =  int(mac[:2], 16), int(mac[2:4], 16), int(mac[4:6], 16), int(mac[6:8], 16), int(mac[8:10], 16), int(mac[10:], 16)

result = f"{mac1:08b}{mac2:08b}{mac3:08b}{mac4:08b}{mac5:08b}{mac6:08b}"
print(result)
