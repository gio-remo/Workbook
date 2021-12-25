# Exercise 1
# Write a program to read through a file and print the contents of the file
# (line by line) all in upper case.

name = input("Filename: ")
try:
    fhand = open(name)
except:
    print("File does not exist.")
    quit()

for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)

# Exercise 2
# Write a program to prompt for a file name, and then read through the file 
# and look for lines of the form: X-DSPAM-Confidence: 0.8475 (https://www.py4e.com/code3/mbox-short.txt)
# When you encounter a line that starts with “X-DSPAM-Confidence:” 
# pull apart the line to extract the floating-point number on the line. 
# Count these lines and then compute the total of the spam confidence values from
# these lines. When you reach the end of the file, print out the 
# average spam confidence.

name = input("Filename: ")
try:
    fhand = open(name)
except:
    print("File does not exist.")
    quit()

count = 0
sum = 0

for line in fhand:
    line = line.rstrip()
    if "X-DSPAM-Confidence" in line:
        print(line)
        i = line.find(" ") + 1
        temp = float(line[i:])
        sum += temp
        count += 1

avg = sum/count
print("Average spam confidence: " + str(avg))