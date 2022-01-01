#####
# L14 - Python Lists
#####

x = [1, 50, "yo"]
print(len(x)) # 3


#####
# L15 - Working with Lists
#####

a = [1, 2]
b = [3, 4]
c = a + b
print(c)

# Create a list
x = list()

x.append(99)
x.append(98)
print(x) # 99, 98

print(99 in x) # True

x.sort()
print(x) # 98, 99

# Some functions take lists as parameters
print(len(x)) # 2
print(max(x)) # 99
print(min(x)) # 98
print(sum(x)) # 197


#####
# L15 - Strings and Lists
#####

stringa = "a black table"
new = stringa.split() # Defualt delimiter ' '
print(new) # It becomes a list