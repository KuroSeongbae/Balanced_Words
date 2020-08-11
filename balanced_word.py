def InputWord():
    print("Give in your word:\n")
    word = input()
    word = word.lower()
    return word

def Occurences(w):
    wordDict = {}
    for i in range(0, len(w)):
        if w[i] != '0' and w[i] != '1' and w[i] != '2' and w[i] != '3' and w[i] != '4' and w[i] != '5' and w[i] != '6' and w[i] != '7' and w[i] != '8' and w[i] != '9':
            if w[i] in wordDict:
                wordDict[w[i]] = wordDict[w[i]] + 1
                counterif = 1
            else:
                addDict = {w[i]: 1}
                wordDict.update(addDict)

    return wordDict

def Balanced(wd):
    isBalanced = True
    for key, value in wd.items():
        if isBalanced == True:
            if value < 2:
                isBalanced = False
    return isBalanced

word = InputWord()
wordDict = Occurences(word)
isBalanced = Balanced(wordDict)

print(word)
print(wordDict)
print(isBalanced)