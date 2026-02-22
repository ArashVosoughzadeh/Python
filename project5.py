def wordcount(sentence):
    allwords = sentence.split()
    cunt={}
    for word in  allwords :
        if word in cunt:
            cunt[word]+=1
        else:
            cunt[word]=1
    return cunt





a=input("pleas Enter your jmle: ")
wordcount(a)
print(wordcount(a))