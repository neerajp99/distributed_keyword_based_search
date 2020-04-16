import json
from datetime import datetime
import random
from collections import defaultdict
# import setdefault
import string

# Simpler method to create a dictionary of a-z characters
# d = dict.fromkeys(string.ascii_lowercase, 0)
# d['a'] = dict.fromkeys(string.ascii_lowercase, 0)
# print(d)


# Parent dictionary
master_dict = defaultdict()
initial = 97
# final = 122
for i in range(26):
	x = chr(initial)
	master_dict[x] = 0
	initial += 1


# Method to generate dictionary
def generateDictionary(text):
	master_dict = {}
	initial = 97
	if text == "":
		for i in range(26):
			x = chr(initial)
			master_dict[x] = 0
			initial += 1
	else:
		for i in range(26):
			x = chr(initial)
			master_dict[x] = 0
			initial += 1

	return master_dict

# Mehtod to create sub strings
def createString(string, dictionary):
    while string.startswith('/'):
        string = string[1:]
    parts = string.split('/', 1)
    if len(parts) > 1:
        branch = dictionary.setdefault(parts[0], {})
        createString(parts[1], branch)
    else:
        if parts[0] in dictionary:
            dictionary[parts[0]] = generateDictionary("")
        else:
        	dictionary[parts[0]] = generateDictionary("")


word = "Mondal"
new_word = word.lower()

for i in range(0, len(word) + 1, 1):
	if i <= len(word):
		current_string = new_word[0:i]
		current_string = '/'.join(list(current_string))
		# Check the string passing is correct below
		# print(current_string)
		createString(current_string, master_dict)

# Final updated dictionary
print(master_dict)
