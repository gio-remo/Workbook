#####
# L15 - Strings in Pyhton
#####

word = "ciao"
letter = word[0]
print(letter) # "c"

for l in word :
    print(l)

# Lenght of strings
print(len(word)) # "4"

# Looping and counting
word = "giovanni"
count = 0
for l in word :
    if l=="n" :
        count+=1
print(count)

#####
# L16 - Intermediate Strings
#####

# Slicing Strings
str = "Ciao come"
print(str[0:4]) # "Ciao"
print(str[6:]) # "ome"

# in Operator
word = "banana"
if "n" in word :
    print(word)

# String Library Methods
word = "BaNaNa"
word1 = word.lower() # lower()
print(word, word1)

word = "banana"
i = word.find("n") # find(), i = 2
print(word[i:]) # "nana"

greet = "ciao gio"
greet = greet.replace("gio", "sis") # replace()
print(greet) # "ciao sis"