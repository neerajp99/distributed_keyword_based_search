from string import ascii_lowercase

def generateDict(val = ""):
    my_dict = dict()
    for i in ascii_lowercase:
        my_dict[val+i] = dict()
    my_dict[val+" "] = dict()
    return my_dict

def insertKeyword(doc_meta, keyword):    
    str = keyword.strip()
    str = str.lower()
    my_str = ""
    val = ""
    for i in range(len(str)):
        temp_dict = generateDict(my_str)
        my_str += str[i]
        if i==len(str)-1:
            temp_dict[my_str][0] = doc_meta
        else:
            temp_dict[my_str][-1] = "node"
        print(temp_dict)
        print("\n")
#print(generateDict("s"))

def insertDoc(doc_meta):
    keywords = doc_meta["keywords"]
    keywords = [x.strip() for x in keywords.split(',')]
    for i in range(len(keywords)):
        #my_keyword = keywords[i].strip()
        print(keywords[i])
        insertKeyword(doc_meta, keywords[i])

doc_meta = dict()
doc_meta["url"] = "https://www.youtube.com"
doc_meta["title"] = "YouTube"
doc_meta["keywords"] = "video, sharing, camera phone, video phone, free, upload"
doc_meta["description"] = "Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube."

insertDoc(doc_meta)
    
