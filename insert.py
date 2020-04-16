# Import Packages
from string import ascii_lowercase
from pathlib import Path
from os import path
import random, string, json, os

#Settings
ext = ".txt"
customDirectory = "files"

dir_path = os.getcwd()
dir_path += "\ ".strip()+customDirectory
if customDirectory!="":
    Path(customDirectory).mkdir(parents=True, exist_ok=True)
    customDirectory += "/"


def cleanDir():
    test = os.listdir(dir_path)
    for item in test:
        if item.endswith(ext):
            os.remove(os.path.join(dir_path, item))
   
            
def commit(data, file_name, newDict, node_index, node, my_str, index_val, doc_meta):
    data = json.dumps(data)
    if newDict==False:
        #print(customDirectory+file_name)
        f_r = open(customDirectory+file_name)
        content = f_r.read()
        f = open(customDirectory+file_name, "w")
        print("Content")
        print(content)
        content = json.loads(content)
        if node == True:
            content[my_str][-1] = node_index
        else:
            content[my_str][index_val] = doc_meta
        content = json.dumps(content)
        f.write(content)
    else:
        f = open(customDirectory+file_name, "w")
        f.write(data)
    #print(data)
    
def generateNodeIndex(str, i):
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
    x = ""
    for j in range(i+1):x += str[j]
    x += ext
    return x

def generateDict(val = ""):
    my_dict = dict()
    for i in ascii_lowercase:
        my_dict[val+i] = dict()
    my_dict[val+" "] = dict()
    return my_dict

def fetchDict(val, str, i, file_name):
    newDict = True
    x = file_name
    try:
        open(customDirectory+x, "r")
        print("\n"+customDirectory+x)
        newDict = False
    except:
        print("\n"+customDirectory+x)
    return generateDict(val), newDict

def getNextVal(temp_dict, my_str):
    x = 0
    for i in range(len(temp_dict[my_str])):
        x += 1
    return x

def tryInsert(temp_dict, my_str, doc_meta, i, str, newDict):
    node = False
    node_index = ""
    index_val = -1
    if i==len(str)-1:
        index_val = getNextVal(temp_dict, my_str)
        temp_dict[my_str][index_val] = doc_meta
    else:
        node_index = generateNodeIndex(str, i)
        temp_dict[my_str][-1] = node_index
        node = True
    return temp_dict, node, node_index, index_val

def insertKeyword(doc_meta, keyword):    
    str = keyword.strip().lower()
    my_str = ""
    val = ""
    file_name = "root"+ext
    node = False
    for i in range(len(str)):
        if node:
            pass
            #print("Node Index: "+node_index)
        temp_dict, newDict = fetchDict(my_str, str, i, file_name)
        print("New File:")
        print(newDict)
        my_str += str[i]
        temp_dict, node, node_index, index_val = tryInsert(temp_dict, my_str, doc_meta, i, str, newDict)
        commit(temp_dict, file_name, newDict, node_index, node, my_str, index_val, doc_meta)
        file_name = node_index
        #print("\n")
    print("Keyword Inserted Successfully: "+str+"\n\n")

def insertDoc(doc_meta):
    keywords = doc_meta["keywords"]
    keywords = [x.strip() for x in keywords.split(',')]
    for i in range(len(keywords)):
        #my_keyword = keywords[i].strip()
        #print("Insert Keyword: "+keywords[i])
        insertKeyword(doc_meta, keywords[i])

cleanDir()
doc_meta = dict()
doc_meta["url"] = "https://www.youtube.com"
doc_meta["title"] = "YouTube"
doc_meta["keywords"] = "video, sharing, camera phone, video phone, free, upload"
doc_meta["description"] = "Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube."
insertDoc(doc_meta)
    
