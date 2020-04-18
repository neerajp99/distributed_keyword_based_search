# Import Packages
from string import ascii_lowercase
from pathlib import Path
from os import path
import random, string, json, os, sys

#Settings
ext = ".txt"
customDirectory = "files"

#Fixed Working Directories
dir_path = os.getcwd()
dir_path += "\ ".strip()+customDirectory
if customDirectory!="":
    Path(customDirectory).mkdir(parents=True, exist_ok=True)
    customDirectory += "/"

def getReturnList(lst):
	my_arr = []
	for i in lst:
		if int(i) > -1:
			my_val = lst[i]
			my_arr.append(my_val)
	
	return my_arr

def leafSearch(my_str, i, keyword, file_name):
	end = False
	f = open(customDirectory+file_name)
	content = f.read()
	#print(customDirectory+file_name)
	content = json.loads(content)
	if i<len(keyword)-1:
		if "-1" in content[my_str].keys():
			pass
		else:
			return -1
		if bool(content[my_str]):
			file_name = content[my_str]["-1"]
		else:
			return -1
	else:
		end = True
		return_lst = getReturnList(content[my_str])
		if bool(content[my_str]) and len(return_lst)>0:
			return return_lst, end		
		else:
			return -1
	#print(file_name)
	return file_name

def searchKeyword(keyword):
	my_str = ""
	file_name = "root"+ext
	found = True
	for i in range(len(keyword)):
		my_str += keyword[i]
		file_name = leafSearch(my_str, i, keyword, file_name)
		#print(file_name)
		if file_name == -1:
			found = False
			break
		#print(my_str)
	if found:
		return file_name
	else:
		return found


search = str(sys.argv[0])

print(searchKeyword(search))
