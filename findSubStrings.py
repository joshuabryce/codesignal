'''
Input:
words: ["Apple",
 "Melon",
 "Orange",
 "Watermelon"]
parts: ["a",
 "mel",
 "lon",
 "el",
 "An"]
Expected Output:
["Apple",
 "Me[lon]",
 "Or[a]nge",
 "Water[mel]on"]
'''

'''
iterate through words find out if parts are in it
iterate through parts find out if parts are in parts
replace instaces of parts within parts with []
'''

def wordInWord(word,part):
    index = word.find(part)
    length = len(part)
    #word = word[index:index+1]
    if(index>-1):
        returnThis=word[0:index] + "[" + part + "]" + word[index + length:len(word)]
        return returnThis
    else:
        return None
    #     return word

def partInWord(word):
    index = word.find('[')
    index2=word.find(']')
    if(index>-1):
        returnthis=word[index:index2]
        return returnthis
    else:
        return None

def findSubstrings(words, parts):
    newWords = []
    maxLength=0

    for i in words:
        currentWord = []
        partsInWord = {}
        #partsInWordIndex = []
        #count=-1
        for j in parts:
            #count+=1
            if i == 'televise' and j == 'ise':
                a = 1
            word=wordInWord(i,j)
            if word != None:
                currentWord.append(word)
                if(partsInWord.get(word.index(j)) == None or len(partsInWord[word.index(j)])<len(j) ):
                    partsInWord[word.index(j)]=j
                #partsInWordIndex.append()
        # countMax=count(p for p in currentWord if len(p) == maxLength)
        # newWords.append(max(currentWord, key=len))
        partsInWordSorted =  sorted(partsInWord, key=partsInWord.get, reverse=False) #partsInWord.items() #.values() #sorted(partsInWord, key=partsInWord.__getitem__) #sorted(partsInWord.items(), key=lambda kv: kv[1])
        #partsInWordSorted2=list(partsInWordSorted)
        if(len(partsInWord)>0):
            # maxWord=max(partsInWord, key=len)
            # maxLength = len(maxWord)
            maxLength= max(len(v) for k, v in partsInWord.items())
            #smallestIndex = min(index(v) for k, v in partsInWord.items())
            #smallestIndex = min(partsInWord.items().All(f= > len(f) = maxLength))
            listPartsInWord = list(partsInWord.values())
            shortPartsInWord = [x for x in listPartsInWord if len(x) == maxLength]
            indexOfShortPartsInWord = [i.index(x) for x in shortPartsInWord]
            smallestIndex = min(indexOfShortPartsInWord)
            #smallestIndex = all(str(i.index(f)) in f for f in shortPartsInWord)
            # max(stats.items(), key=operator.itemgetter(1))[0]
            # maxLength=len(maxWord)-1-maxWord.index('[')-

            for j in partsInWordSorted:
                if i == 'televise':
                    a=1

                if len(partsInWord[j]) == maxLength and i.index(partsInWord[j]) == smallestIndex:
                    appendWord=wordInWord(i,partsInWord[j])
                    if appendWord != None:
                        newWords.append(appendWord)
                        break
        else:
            newWords.append(i)
        #newWords.append(max(currentWord,key=len))
        # values=currentWord.index(max(currentWord,key=len))
        # print(values)
        #newWords.append(currentWord[values.index(min(values))])
        # else:
        #     newWords.append(i)
    #return wordInWord("Melon","lon")
    return newWords
# print(findSubstrings)

#
# def findSubstrings(words, parts):
#     returnthis =[]
#     for i in words:
#         # partsIndex={}
#         wordsInParts=set()
#         word = ""
#         for j in parts:
#             for b in wordsInParts:
#                 index = b.index(j)
#
#             if j in i:
#                 # index=i.index(j)
#                 #print(index)
#                 # partsIndex.update(index,j)
#                 wordsInParts.add(j)
#
#         print(partsIndex)


# words=["Apple",
#  "Melon",
#  "Orange",
#  "Watermelon"]
# parts= ["a",
#  "mel",
#  "lon",
#  "el",
#  "An"]


words= ["neuroses",
 "myopic",
 "sufficient",
 "televise",
 "coccidiosis",
 "gules",
 "during",
 "construe",
 "establish",
 "ethyl"]
parts= ["aaaaa",
 "Aaaa",
 "E",
 "z",
 "Zzzzz",
 "a",
 "mel",
 "lon",
 "el",
 "An",
 "ise",
 "d",
 "g",
 "wnoVV",
 "i",
 "IUMc",
 "P",
 "KQ",
 "QfRz",
 "Xyj",
 "yiHS"]

output=findSubstrings(words, parts)
print(output)

expected = ["neuroses",
 "myop[i]c",
 "suff[i]cient",
 "telev[ise]",
 "cocc[i]diosis",
 "[g]ules",
 "[d]uring",
 "construe",
 "est[a]blish",
 "ethyl"]