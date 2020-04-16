# Import Packages
from string import ascii_lowercase
from pathlib import Path
from os import path
import random, string, json, os
import csv

#Settings
ext = ".txt"
customDirectory = "files"

#Fixed Working Directories
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
   
def strtoint(lst):
    for i in range(0, len(lst)): 
        lst[i] = int(lst[i])    
    return lst       

def commit(data, file_name, newDict, node_index, node, my_str, index_val, doc_meta):
    data = json.dumps(data)
    add = True
    if newDict==False:
        f_r = open(customDirectory+file_name)
        content = f_r.read()
        content = json.loads(content)
        f = open(customDirectory+file_name, "w")
        if node == True:
            content[my_str]["-1"] = node_index
        else:
            x = 0
            my_keys = len(list(content[my_str]))
            #my_keys = max(strtoint(my_keys))
            for i in range(my_keys):
                #print(list(content[my_str]).index(str(i)))
                if list(content[my_str])[i]=="-1":
                    continue
                else:
                    try:
                        if "url" in content[my_str][str(i)]:
                            x += 1
                            if content[my_str][str(i)]["url"]==doc_meta["url"]:
                                content[my_str][str(i)] = doc_meta
                                
                                add = False
                                break
                    except KeyError:
                        continue
            if add:
                content[my_str][str(x+1)] = doc_meta
        content = json.dumps(content)
        f.write(content)
    else:
        f = open(customDirectory+file_name, "w")
        f.write(data)
    
def generateNodeIndex(str, i):
    #x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
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
        newDict = True
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
    #str = str.replace(" ", "$")
    my_str = ""
    val = ""
    file_name = "root"+ext
    node = False
    for i in range(len(str)):
        temp_dict, newDict = fetchDict(my_str, str, i, file_name)
        print("New File:")
        print(newDict)
        my_str += str[i]
        temp_dict, node, node_index, index_val = tryInsert(temp_dict, my_str, doc_meta, i, str, newDict)
        commit(temp_dict, file_name, newDict, node_index, node, my_str, index_val, doc_meta)
        file_name = node_index
    print("Keyword Inserted Successfully: "+str+"\n\n")

def insertDoc(doc_meta):
    keywords = doc_meta["keywords"]
    keywords = [x.strip() for x in keywords.split(',')]
    for i in range(len(keywords)):
        insertKeyword(doc_meta, keywords[i])

# cleanDir()
# doc_meta = dict()
# doc_meta["url"] = "https://www.youtube.com"
# doc_meta["title"] = "YouTube"
# doc_meta["keywords"] = "search, video, sharing, camera phone, video phone, free, upload"
# doc_meta["description"] = "Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube."
# insertDoc(doc_meta)

# doc_meta2 = dict()
# doc_meta2["url"] = "https://in.yahoo.com"
# doc_meta2["title"] = "Yahoo India | News, Finance, Cricket, Lifestyle and Entertainment"
# doc_meta2["keywords"] = "search, yahoo, yahoo home page, yahoo homepage, yahoo search, yahoo mail, yahoo messenger, yahoo games, news, finance, sport, entertainment"
# doc_meta2["description"] = "Get latest news, email, live cricket scores and fresh finance, lifestyle, entertainment content daily."
# insertDoc(doc_meta2)

# Test Data 

# json_data_path = pathlib.Path(__file__).parent.absolute()
json_data_path = str(Path().absolute())
path_to_find = json_data_path + "/scrap_synonyms/scrap_synonyms/data.csv"

# # Open the json file 
# with open(path_to_find) as fi:
#     data_content = json.loads(fi.read())
# print(data_content[0]['url'])

with open(path_to_find, mode = 'r') as fi:
    data_content = csv.reader(fi, delimiter=',')
    for line in data_content:
        doc_meta = dict()
        doc_meta["url"] = line[0]
        doc_meta["title"] = line[1]
        doc_meta["keywords"] = line[2]
        doc_meta["description"] = line[3]
        insertDoc(doc_meta)

# Loop over the data, and call the insertDoc operation 

# for i in range(len(data_content)):
#     doc_meta = dict()
#     doc_meta["url"] = data_content[i]['url']
#     doc_meta["title"] = data_content[i]['title']
#     doc_meta["keywords"] = data_content[i]['keywords']
#     doc_meta["description"] = data_content[i]['description']
#     insertDoc(doc_meta)
    
