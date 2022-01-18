# -*- coding: utf-8 -*-
"""
Task 7.3b

Make a copy of the code from the task 7.3a.

Add this functionality:
- Ask the user to enter the VLAN number.
- Print information only for the specified VLAN.

Output example:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
vlan_num = int(input("Enter VLAN number:"))


with open('CAM_table.txt') as src:
    output = src.readlines()

line_list = []
for line in output:
    line = line.split()
    #Remove empty lines and those that don't start with a digit
    if len(line) != 0 and line[0].isdigit():
        #Turn the vlan into a number for sorting
        line[0] =  int(line[0])
        #Append the line to a new list
        line_list.append(line)
        #Sort list in place
        line_list.sort()

#Create and print output from sorted list
for line in line_list:
    vlan = line[0]
    mac = line[1]
    int = line[3]
    if vlan_num == vlan:
        print('{:<8}{:<}{:>8}'.format(vlan, mac, int))
