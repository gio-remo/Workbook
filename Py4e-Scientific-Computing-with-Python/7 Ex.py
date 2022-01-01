# Exercise 4: Find all unique words in a file
# https://www.py4e.com/code3/romeo.txt

str = input("Enter a file: ")

fhand = ""
try:
    fhand = open(str)
except:
    print("File not found")

unique = []
for line in fhand :
    line = line.rstrip()
    splitted = line.split()

    for i in splitted :
        if i not in unique :
            unique.append(i)

unique.sort()
print(unique)


# Exercise 5: Minimalist Email Client
# https://www.py4e.com/code3/mbox-short.txt

fhand = open("test.txt")

senders = []
for line in fhand :
    line = line.rstrip()

    if line.startswith("From ") :
        splitted = line.split()
        senders.append(splitted[1])

print(len(senders), "new emails")