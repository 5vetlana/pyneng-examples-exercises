# -*- coding: utf-8 -*-
"""
Task 6.2b

Make a copy of the code from the task 6.2a.

Add this functionality: If the address was entered incorrectly, request the address again.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
valid_ip = False

while not valid_ip:

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
