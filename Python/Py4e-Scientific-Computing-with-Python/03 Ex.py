# Exercise 4.6:
# Rewrite your pay computation with time-and-a-half for overtime and create
# a function called computepay which takes two parameters (hours and rate)

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

def computepay(h, r):
    if h>40 :
        extra=h-40
        pay = (h-extra)*r + extra*(r*1.5)
        return pay
    else :
        return h*r

print("Pay: " + str(computepay(fhours, frate)))


# Exercise 7:
# Rewrite the grade program from the previous chapter
# using a function called computegrade that takes a score as its
# parameter and returns a grade as a string.

def computegrade(s):
    if s<0.6:
        return "F"
    elif s>=0.6 and s<0.7:
        return "D"
    elif s>=0.7 and s<0.8:
        return "C"
    elif s>=0.8 and s<0.9:
        return "B"
    elif s>=0.9:
        return "A"

fscore=-1

while fscore<0 or fscore>1 :
    rscore=input("Enter score: ")
    try:
        fscore=float(rscore)
    except:
        fscore=-1
        print("Bad score")

print(computegrade(fscore))