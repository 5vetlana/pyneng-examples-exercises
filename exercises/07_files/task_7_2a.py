# -*- coding: utf-8 -*-
"""
Task 7.2a

Make a copy of the code from the task 7.2.

Add this functionality: The script should not print to the stdout commands,
which contain words from the ignore list.

The script should also not print lines that begin with !.

Check the script on the config_sw1.txt configuration file.
The filename is passed as an argument to the script.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

ignore = ["duplex", "alias", "configuration"]

with open("config_sw1.txt") as f:
    output = f.readlines()

for line in output:
    #Split line into words
    words = line.split()
    #Find intersection points in both words and the ignore list
    intersect = set(words) & set(ignore)
    #If lines don't start with ! or a word in the ignore list print the line
    if not line.startswith("!") and not intersect:
        line = line.rstrip()
        print(line)
