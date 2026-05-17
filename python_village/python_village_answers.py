# ======python village answers======


# 	1 - Installing Python

import this



# 	2 - Variables and Some Arithmetic	

a = 3
b = 5
print(a**2 + b**2)



# 	3 - Strings and Lists

given_string = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'
print(given_string[22:28], given_string[97:103])



# 	4 - Conditions and Loops

c = 100
d = 200
e = 0
for x in range(c, d+1):
	if x%2!=0:
		e += x

print(e)



# 	5 - Working with Files

f = open('input.txt', 'r')

for index, value in enumerate(f):
	if index%2!=0:
		print(value.strip())



#	6 - Dictionaries

sample_dataset = 'We tried list and we tried dicts also we tried Zen'
count = {}

for word in sample_dataset.split():		#.split() seperates the string by the spaces (returns words) instead of by characters
	if word in count:
		count[word] += 1
	else:
		count[word] = 1 	#counter can be used here instead of if/else logic

for word, freq in count.items(): 	#.items() returns all key/value pairs in the dict rather than having them both in one tuple. can be under any name (e.g. word/ freq)
		print(word, freq)
