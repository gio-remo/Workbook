# Exercise 3.1:
# Rewrite your pay computation to give the employee 1.5 times the hourly
# rate for hours worked above 40 hours.

hours=input("Enter hours: ")
rate=input("Enter rate: ")

hours=float(hours)
rate=float(rate)
pay=0

if hours>40 :
    extra=hours-40
    pay = (hours-extra)*rate + extra*(rate*1.5)
else :
    pay = hours*rate

print("Pay: " + str(pay))


# Exercise 3.2:
# Rewrite your pay program using try and except so that your program handles
# non-numeric input gracefully by printing a message and exiting the program

fhours=-1

while fhours<0 :
    hours=input("Enter hours: ")
    try :
        fhours=float(hours)
    except :
        fhours=-1
        print("Error, please enter numeric input")

frate=-1

while frate<0 :
    rate=input("Enter rate: ")
    try :
        frate=float(rate)
    except :
        frate=-1
        print("Error, please enter numeric input")

pay=0

if fhours>40 :
    extra=fhours-40
    pay = (fhours-extra)*frate + extra*(frate*1.5)
else :
    pay = fhours*frate

print("Pay: " + str(pay))


# Exercise 3.3:
# Write a program to prompt for a score between 0.0 and 1.0. If the score is 
# out of range, print an error message. If the score is between 0.0 and 1.0, 
# print a grade using the following table:
#  Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

fscore=-1

while fscore<0 or fscore>1 :
    rscore=input("Enter score: ")
    try:
        fscore=float(rscore)
    except:
        fscore=-1
        print("Bad score")

if fscore<0.6:
    print("F")
elif fscore>=0.6 and fscore<0.7:
    print("D")
elif fscore>=0.7 and fscore<0.8:
    print("C")
elif fscore>=0.8 and fscore<0.9:
    print("B")
elif fscore>=0.9:
    print("A")