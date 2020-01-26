import sys

# # the runtime for my tokenize function is O(n) because I go through
# the whole document once pairing characters together into words
def tokenize(path):

    # if either of the files is empty then we have 0 common tokens and the program should end
    c=path.read(1)
    if(len(c)==0):
        print(0)
        sys.exit(0)
    tokenList = []
    count=0
    word = ""
    while True:
        if(count==0):
            char=c
            count+=1
        else:
            char = path.read(1)
        if ((char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or (char >= '0' and char <= '9')):
            word += char.lower()
        elif not char:
            break
        else:
            if (len(word)) > 0:
                tokenList.append(word)
                word = ""

    return tokenList

# the runtime for my computeWordFrequencies function is O(n) since dict in lookups
# are O(1)avg and we loop through n terms
def  computeWordFrequencies(tokens):

    dict={}
    # for tokens in our list
    for i in tokens:
        # if token exists in the dictionary add one to frequencie
        if i in dict:
            dict[i] += 1
        # if does not exist then at that key set value to 1
        else:
            dict[i] = 1

    return dict

# the runtime of this function is O(n) because the in lookup for a dictionary
# is O(1) average and we do it for n times
def wordSimilaraties(freq1, freq2):
    count = 0;
    for i in freq1:
        if i in freq2:
            count += 1
    print(count)

# here I try to open both files if one fails then I end the program since it
# is most likely a wrong path passed in
def main():
    temp=sys.argv[1]
    temp1=sys.argv[2]
    k=len(temp)
    t=len(temp1)
    if(temp[k-1]!='t'and temp[k-2]!='x'and temp[k-3]!='t'):
        sys.exit(0)
    if (temp1[t - 1] != 't' and temp1[t - 2] != 'x' and temp1[t - 3] != 't'):
        sys.exit(0)
    try:
        file0 = open(temp, "r", encoding='ascii', errors='replace')
    except:
        sys.exit(0)
    try:
        file1 = open(temp1, "r", encoding='ascii', errors='replace')
    except:
        sys.exit(0)
    tokens = tokenize(file0)
    tokens2 = tokenize(file1)
    tokens = computeWordFrequencies(tokens)
    tokens2 = computeWordFrequencies(tokens2)
    wordSimilaraties(tokens,tokens2)
    file0.close()
    file1.close()

if __name__ == "__main__":
    main()
