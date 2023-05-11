# Exercise 2
# Write a program that categorizes each mail message by which day of the week the commit was done.
# (https://www.py4e.com/code3/mbox-short.txt)

fhand = open("test.txt")

days = dict()

for line in fhand :

    if line.startswith("From ") :
        v = line.split()

        if v[2] not in days :
            days[v[2]] = 1
        else :
            days[v[2]] += 1

print(days)
fhand.close()


# Exercise 3
# Write a program to read through a mail log, count how many messages have come from each email address, and print the dictionary.
# (https://www.py4e.com/code3/mbox-short.txt)

fhand = open("test.txt")

emails = dict()

for line in fhand :

    if line.startswith("From ") :
        v = line.split()

        if v[1] not in emails :
            emails[v[1]] = 1
        else :
            emails[v[1]] += 1

print(emails)
fhand.close()

# Exercise 4
# Add code to the above program to figure out who has the most messages in the file.

fhand = open("test.txt")

emails = dict()

for line in fhand :

    if line.startswith("From ") :
        v = line.split()

        if v[1] not in emails :
            emails[v[1]] = 1
        else :
            emails[v[1]] += 1

max_val = None
max_key = None

for i in emails :

    if max_val is None :
        max_val = emails[i]
        max_key = i
    elif emails[i] > max_val :
        max_val = emails[i]
        max_key = i

print(max_key, max_val)
fhand.close()