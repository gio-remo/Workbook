####
# L4 - Introduction: Elements of Python
####

# Sequenziali

x=2
x=x+2
print(x)

# Conditional

x=11
if x < 10:
    print("Piccolo")
else:
    print("Grande")

y=21
if y<10:
    print("Piccolo")
elif y>=10 | y<=20:
    print("Grande")
else:
    print("Grandissimo")

# Repeated

n=5
while n>0:
    print("Colpito")
    n-=1
    print("Vite rimaste: " + str(n))
print("Ucciso")

####
# L6 - Intermediate Expressions
####

# ** potenza
# % resto

print(10%2) # resto 0
print(10%3) # resto 1
print(10%4) # resto 2

a="ciao" 
type(a) # str

b=20 
type(b) # int

c=20.10
type(c) # float

print(float(99) + 100) # 199.0

print(10/2) # 5.0 => division produces a FLOAT result

# String conversion
a="21"
type(a) # str
a=int(a)
type(a) # int
print(a+1)

# User input
name = input('Nome: ')
print("Ciao ", name)