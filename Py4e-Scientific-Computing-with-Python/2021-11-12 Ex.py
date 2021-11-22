# Exercise 5.1:
# Write a program which repeatedly reads numbers until the user enters “done”. 
# Once “done” is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using 
# try and except and print an error message and skip to the next number.

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