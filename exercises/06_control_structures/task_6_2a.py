# -*- coding: utf-8 -*-
"""
Task 6.2a

Make a copy of the code from the task 6.2.

Add verification of the entered IP address.
An IP address is considered correct if it:
    - consists of 4 numbers (not letters or other symbols)
    - numbers are separated by a dot
    - every number in the range from 0 to 255

If the IP address is incorrect, print the message: 'Invalid IP address'

The message "Invalid IP address" should be printed only once,
even if several points above are not met.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
try:
    ip_address = input("Enter an IP address in the format 10.1.1.1: ")
    ip_addr = ip_address.split('.')


    valid_ip = len(ip_addr) == 4

    for num in ip_addr:
        valid_ip = num.isdigit() and 0 <= int(num) <= 255 and valid_ip

    oct1 = ip_addr[0]
    oct1 = int(oct1)

#For exception wlhere "." is not used as a separeator
except:
    print("Invalid IP Address")

else:
    if valid_ip:
        if 1 <= oct1 <= 223:
            print("unicast")
        elif 224 <= oct1 <= 239:
            print("multicast")
        elif ip_address == "255.255.255.255":
            print('local broadcast')
        elif ip_address == "0.0.0.0":
            print('unassiged')
        else:
            print('unused')
    else:
        print("Invalid IP Addresss")
