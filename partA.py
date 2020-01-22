import re
import sys

def tokenize(path):
    file0 = open(path, "r", encoding='ascii', errors='replace')
    tokenList = []
    tempLine = file0.readlines()

    for x in tempLine:
        #token = re.findall(r'[^\W_]+', x)
        token = re.findall(re.compile(r"[a-z0-9]+", re.IGNORECASE),x)
        tokenList +=token

    tokenList = [x.lower().strip() for x in tokenList]
    file0.close()
    return tokenList

def  computeWordFrequencies(tokens):

    temp = []
    dict={}
    for i in tokens:
        if i not in temp:
            temp.append(i)
    for i in range(0,len(temp)):
        dict[temp[i]]=tokens.count(temp[i])
    return dict

def mapPrint(myMap):
    sortedMap = sorted(myMap,key=myMap.get,reverse=True)

    for i in sortedMap:
        print(i,"->",myMap[i])


def main():
    textPath = sys.argv[1]
    tokens = tokenize(textPath)
    tokenMap = computeWordFrequencies(tokens)
    mapPrint(tokenMap)

if __name__ == "__main__":
    main()


