####
# L9 - Python Functions
####

def thing():
    print("Hello")
    print("Fun")

thing()


def welcome(n):
    print("Hello " + n)

name=input("Name: ")
welcome(name)


#####
# L10 - Build your own Functions
#####

def greet(l):
    if l=='i':
        print("Ciao")
    elif l=='e':
        print("Hi")
    elif l=='s':
        print("Hola")
    else:
        print("Not a lang")

lang=input("Select lang (i/e/s): ")
greet(lang)


def greet1():
    return "Hi"

print(greet1(), "Giorgio")