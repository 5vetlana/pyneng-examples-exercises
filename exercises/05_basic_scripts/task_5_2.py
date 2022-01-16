# -*- coding: utf-8 -*-
"""
Task 5.2

Ask the user to enter the IP network in the format: 10.1.1.0/24

Then print information about the network and mask in this format:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different net/mask combinations.

Hint: You can get the mask in binary format like this:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

You can then take 8 bits of the binary mask using slices and convert them to decimal.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
network_and_sub = input('Enter the IP network in the format 10.1.1.0/24: ')
ip_address, mask = network_and_sub.split('/')
oct_list = ip_address.split('.')
oct1 = int(oct_list[0])
oct2 = int(oct_list[1])
oct3 = int(oct_list[2])
oct4 = int(oct_list[3])

mask = int(mask)
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
