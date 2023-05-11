####
# L7 - Conditional Execution
####

x=4
if x>2 :
    print("Bigger")
else :
    print("Smaller")

####
# L8 - More Conditional Structures
####

x=11
if x<2 :
    print("Small")
elif x<10 :
    print("Medium")
else :
    print("Large")

# try / except

text="Hello"
try:
    istr=int(text)
except:
    istr=-1 # if it fails, flag

rawstr=input("Enter a number: ")
try :
    val=int(rawstr)
except :
    val=-1

if val>0 :
    print("Ok")
else :
    print("NAN")