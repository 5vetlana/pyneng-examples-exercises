# -*- coding: utf-8 -*-
"""
Task 5.2a

Copy and modify the script from task 5.2 so that, if the user entered a host address
rather than a network address, convert the host address to a network address
and print the network address and mask, as in task 5.2.

An example of a network address (all host bits are equal to zero):
* 10.0.1.0/24
* 190.1.0.0/16

Host address example:
* 10.0.1.1/24 - host from network 10.0.1.0/24
* 10.0.5.195/28 - host from network 10.0.5.192/28

If the user entered the address 10.0.1.1/24, the output should look like this:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different host/mask combinations, for example:
    10.0.5.195/28, 10.0.1.1/24

Hint:
The network address can be calculated from the binary host address and the netmask.
If the mask is 28, then the network address is the first 28 bits host addresses + 4 zeros.
For example, the host address 10.1.1.195/28 in binary will be:
bin_ip = "00001010000000010000000111000011"

Then the network address will be the first 28 characters from bin_ip + 0000
(4 because in total there can be 32 bits in the address, and 32 - 28 = 4)
00001010000000010000000111000000

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

network_and_sub = input('Enter the IP network in the format 10.1.1.0/24: ')
#Split user input to ip and mask
ip_address, mask = network_and_sub.split('/')
#Split the ip address input into octexts
oct1, oct2, oct3, oct4 = ip_address.split('.')
#Convert octets to binary 8 value sets and convert taht to a sting
bin_ip = '{:08b}{:08b}{:08b}{:08b}'.format(int(oct1), int(oct2), int(oct3), int(oct4))
#Convert mask to interger
mask = int(mask)
network_ip = bin_ip[0:mask] + "0" * (32 - mask)

oct1 = int(network_ip[:8], 2)
oct2 = int(network_ip[8:16], 2)
oct3 = int(network_ip[16:24], 2)
oct4 = int(network_ip[24:], 2)

full_mask =  "1" * mask + "0" * (32 - mask)
mask_oct1 = int(full_mask[:8], 2)
mask_oct2 = int(full_mask[8:16],2)
mask_oct3 = int(full_mask[16:24], 2)
mask_oct4 = int(full_mask[24:],2)

ip_template = '''
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{4:<8}
{5:<8}  {6:<8}  {7:<8}  {8:<8}
{5:08b}  {6:08b}  {7:08b}  {8:08b}
'''

print(ip_template.format(oct1, oct2, oct3, oct4, mask, mask_oct1, mask_oct2, mask_oct3, mask_oct4))
