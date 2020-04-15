import random, string
            
def generateNodeIndex():
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
    return x

def generateDict(val = ""):
    my_dict = dict()
    for i in ascii_lowercase:
        my_dict[val+i] = dict()
    my_dict[val+" "] = dict()
    return my_dict

def getNextVal(temp_dict, my_str):
    x = 0
    for i in range(len(temp_dict[my_str])):
        x += 1
    return x

def tryInsert(temp_dict, my_str, doc_meta, i, str):
    node = False
    node_index = generateNodeIndex()
    if i==len(str)-1:
        index_val = getNextVal(temp_dict, my_str)
        temp_dict[my_str][index_val] = doc_meta
    else:
        temp_dict[my_str][-1] = node_index
        node = True
    return temp_dict, node, node_index

def insertKeyword(doc_meta, keyword):    
    str = keyword.strip().lower()
    my_str = ""
    val = ""
    node = False
    for i in range(len(str)):
        if node==True:
            print("Node Index: "+node_index)
        temp_dict = generateDict(my_str)
        my_str += str[i]
        temp_dict, node, node_index = tryInsert(temp_dict, my_str, doc_meta, i, str)
        print(temp_dict)
        print("\n")

def insertDoc(doc_meta):
    keywords = doc_meta["keywords"]
    keywords = [x.strip() for x in keywords.split(',')]
    for i in range(len(keywords)):
        #my_keyword = keywords[i].strip()
        print("Insert Keyword: "+keywords[i])
        insertKeyword(doc_meta, keywords[i])

doc_meta = dict()
doc_meta["url"] = "https://www.youtube.com"
doc_meta["title"] = "YouTube"
doc_meta["keywords"] = "video, sharing, camera phone, video phone, free, upload"
doc_meta["description"] = "Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube."

insertDoc(doc_meta)
    
