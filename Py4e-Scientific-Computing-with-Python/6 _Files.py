#####
# L13 - Reading Files
#####

# open()
# fhand = open(filename, mode)

#####
# L14 - Files as a sequence
#####

# Printing lines
fhand = open("doc.txt")
for line in fhand :
    line = line.rstrip()
    print(line)
fhand.close()

# Counting lines
fhand = open("doc.txt")
count = 0
for line in fhand :
    count+=1
print(count)
fhand.close()

# Reading the whole file
fhand = open("doc.txt")
str = fhand.read()
print(str)
fhand.close()