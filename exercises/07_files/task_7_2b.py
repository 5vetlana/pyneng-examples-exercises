# -*- coding: utf-8 -*-
"""
Task 7.2b

Make a copy of the code from the task 7.2a.
Add this functionality: instead of printing to stdout,
the script should write the resulting lines to a file.

File names must be passed as arguments to the script:
  1. name of the source configuration file
  2. name of the destination configuration file

In this case, the lines that are contained in the ignore list and lines
that start with ! must be filtered.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

ignore = ["duplex", "alias", "configuration"]

with open("config_sw1.txt") as src, open("result.txt", "w") as dest:
    output = src.readlines()
    for line in output:
        #Split line into words
        words = line.split()
        #Find intersection points in both words and the ignore list
        intersect = set(words) & set(ignore)
        #If lines don't start with ! or a word in the ignore list print the line
        if not line.startswith("!") and not intersect:
            dest.write(line)
