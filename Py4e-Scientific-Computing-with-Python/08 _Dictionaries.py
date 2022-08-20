#####
# L22 - Python Dictionaries
#####

bag = dict()

bag['a'] = 12
bag['b'] = 8

print(bag)
print(bag['a'])

other = { }
print(other)


#####
# L23 - Dictionaries: Common Applications
#####

d = dict()
print('key' in d) # False

counts = dict()
names = ['al', 'ol', 'al', 'il', 'il']
for n in names :
    if n not in counts :
        counts[n] = 1
    else :
        counts[n] += 1


print(counts)
print(counts.get('al')) # 2


#####
# L24 - Dictionaries and Loops
#####

bag = dict()

bag['a'] = 12
bag['b'] = 8

print(bag.keys())
print(bag.values())