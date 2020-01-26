import sys

# the runtime for my tokenize function is O(n) because I go through
# the whole document once pairing characters together into words
def tokenize(path):
    k=len(path)
    # if the file is not a .txt format then dont accept it
    if(path[k-1]!='t'and path[k-2]!='x'and path[k-3]!='t'):
        sys.exit(0)
    try:
        file0 = open(path, "r",encoding='ascii', errors='replace')
    except:
        sys.exit(0)

    tokenList = []
    word = ""
    while True:
        char = file0.read(1)
        if ((char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or (char >= '0' and char <= '9')):
            word+=char.lower()
        elif not char:
            break
        else:
            if (len(word)) > 0:
                tokenList.append(word)
                word=""
    file0.close()
    return tokenList

# the runtime for my computeWordFrequencies function is O(n) since dict in lookups
# are O(1)avg and we loop through n terms
def  computeWordFrequencies(tokens):

    # if token is in the dict already increment by 1. if not add and increment by 1
    dict={}
    for i in tokens:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

# the runtime for my mapPrint function is O(n log n)
# O(n) to print and O(logn) to sort
def mapPrint( myMap ):
    sortedMap = sorted(myMap, key=myMap.get, reverse=True)

    for i in sortedMap:
        print(i,"->",myMap[i])

def main():
    textPath = sys.argv[1]
    tokens = tokenize(textPath)
    tokenMap = computeWordFrequencies(tokens)
    mapPrint(tokenMap)

if __name__ == "__main__":
    main()

