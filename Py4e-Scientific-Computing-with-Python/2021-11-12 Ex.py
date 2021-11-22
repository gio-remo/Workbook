# Exercise 5.1
# Write a program which repeatedly reads numbers until the user enters “done”. 
# Once “done” is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using 
# try and except and print an error message and skip to the next number.
"""""
sum = 0
count = 0

while True:
    r_str = input("Enter a number: ")

    if r_str == "done":
        try:
            print("Count:", count, " Sum:", sum, " Avg:", sum/count)
            break
        except ZeroDivisionError:
            print("Numbers missing")
            continue

    try:
        num = int(r_str)
    except:
        print("Invalid input")
        continue
    
    count += 1
    sum += num
"""

# Exercise 5.2
# Write another program that prompts for a list of numbers as above and at 
# the end prints out both the maximum and minimum of the numbers.

small = None
big = None

while True:
    r_str = input("Enter a number: ")

    if r_str == "done":
        print("Smallest:", small, " Biggest:", big)
        break

    try:
        num = int(r_str)
    except:
        print("Invalid input")
        continue
    
    if small is None:
        small = num
    elif num < small:
        small = num

    if big is None:
        big = num
    elif num > big:
        big = num