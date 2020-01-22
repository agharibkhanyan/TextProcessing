import re
import sys

def tokenize(path):
    file0 = open(path, "r", encoding='ascii', errors='replace')
    tokenList = []
    tempLine = file0.readlines()

    for x in tempLine:
        token = re.findall(r'[^\W_]+', x)
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

def wordSimilaraties(freq1, freq2):
    #sortedMap1 = sorted(freq1,key=freq1.get,reverse=True)
    #sortedMap2 = sorted(freq2,key=freq2.get,reverse=True)

    #if(len(sortedMap1)>len(sortedMap2)):
    #listSim = []
    #count = 0
    #for i in freq1+freq2:
     #   if i in freq1 and i in freq2:
      #      listSim.append(i)
       #     count+=1
    #listSim = [i for i in freq1 + freq2 if i in freq1 and i in freq2]
    #listSim = list(dict.fromkeys(listSim))
    freq1 = set(dict.fromkeys(freq1))
    freq2 = set(dict.fromkeys(freq2))
    print(len(freq1.intersection(freq2)))

    #print(len(listSim))

"""def main():
    textPath = sys.argv[1]
    tokens = tokenize(textPath)
    tokenMap = computeWordFrequencies(tokens)
    mapPrint(tokenMap)

if __name__ == "__main__":
    main()"""

tokens1 = tokenize("test.txt")
tokens2 = tokenize("test2.txt")
#freq1 = computeWordFrequencies(tokens1)
#freq2 = computeWordFrequencies(tokens2)
tokens1 = list(dict.fromkeys(tokens1))
tokens2 = list(dict.fromkeys(tokens2))
wordSimilaraties(tokens1,tokens2)




