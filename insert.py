# Import Packages
from string import ascii_lowercase
from pathlib import Path
from os import path
import random, string, json, os, unidecode, csv

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
    enum = True
    x = 0
    #print(temp_dict[my_str])
    try:
        for i in range(len(temp_dict[my_str])):
            x += 1
    except:
        enum = False
    return x, enum

def tryInsert(temp_dict, my_str, doc_meta, i, str, newDict):
    node = False
    enum = True
    node_index = ""
    index_val = -1
    if i==len(str)-1:
        index_val, enum = getNextVal(temp_dict, my_str)
        try:
            temp_dict[my_str][index_val] = doc_meta
        except:
            enum = False
    else:
        node_index = generateNodeIndex(str, i)
        try:
            temp_dict[my_str][-1] = node_index
        except KeyError:
            enum = False
        node = True
    return temp_dict, node, node_index, index_val, enum

def refineKeyword(keyword):
    str1 = keyword.strip().lower()
    str1 = str1.replace(".", " ")
    str1 = str1.replace("-", " ")
    str1 = str1.replace(";", " ")
    str1 = str1.replace("&", " and ")
    str1 = unidecode.unidecode(str1)
    str1.encode('ascii', 'ignore')
    print(str1)
    return str1

def insertKeyword(doc_meta, keyword):    
    print(keyword)
    str = refineKeyword(keyword)
    my_str = ""
    val = ""
    file_name = "root"+ext
    node = False
    for i in range(len(str)):
        temp_dict, newDict = fetchDict(my_str, str, i, file_name)
        print("New File:")
        print(newDict)
        my_str += str[i]
        temp_dict, node, node_index, index_val, enum = tryInsert(temp_dict, my_str, doc_meta, i, str, newDict)
        if enum:
            try:
                commit(temp_dict, file_name, newDict, node_index, node, my_str, index_val, doc_meta)
            except:
                pass
            file_name = node_index
    print("Keyword Inserted Successfully: "+str+"\n\n")

def insertDoc(doc_meta):
    keywords = doc_meta["keywords"]
    keywords = [x.strip() for x in keywords.split(',')]
    for i in range(len(keywords)):
        if keywords[i].isalnum() and keywords[i][0]!="c":
            insertKeyword(doc_meta, keywords[i])

def jsonread():
    # json_data_path = pathlib.Path(__file__).parent.absolute()
    json_data_path = str(Path().absolute())
    path_to_find = json_data_path + "/data/check1.json"

    # Open the json file 
    with open(path_to_find) as fi:
        data_content = json.loads(fi.read())
    # print(data_content[0]['url'])

    # Loop over the data, and call the insertDoc operation 

    for i in range(len(data_content)):
        doc_meta = dict()
        doc_meta["url"] = data_content[i]['url']
        doc_meta["title"] = data_content[i]['title']
        doc_meta["keywords"] = data_content[i]['keywords']
        doc_meta["description"] = data_content[i]['description']
        if data_content[i]['keywords']!="":
            insertDoc(doc_meta)

def csvread():
    with open('data/book.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                doc_meta = dict()
                doc_meta["url"] = row[0]
                doc_meta["title"] = row[1]
                doc_meta["keywords"] = row[2]
                doc_meta["description"] = row[3]
                if doc_meta['keywords']!="":
                    insertDoc(doc_meta)
                line_count += 1
                break

cleanDir()
csvread()
