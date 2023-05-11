#####
# L27 - Regular Expressions
#####

import re

fhand = open("test.txt")
for l in fhand :
    l = l.rstrip()
    if re.search("From:", l) : # l.find("From:")
        print(l)

for l in fhand :
    l = l.rstrip()
    if re.search("^From:", l) : # l.stratswith("From:")
        print(l)

# ^X.*:
# ^X starts with X
# . followed by any charater
# * many times
# : then a column

#####
# L28 - Regular Expressions: Matching and Extracting Data
#####

# re.search() returns True/False
# re.findall() retruns list of matches

# [0-9]+
# + one or more
# digits from 0 to 9

x = "Hi here 2 numbers: 60 and 34"
print(re.findall("[0-9]+", x)) # ['2', '60', '34']

hand = open("test.txt")
for line in hand :
    line = line.rstrip()
    y = re.findall('\S+@\S+', line)
    print(y) # prints only emails ...@...