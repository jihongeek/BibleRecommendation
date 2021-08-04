# preprocessing bible verses
from nltk.stem import WordNetLemmatizer,PorterStemmer,LancasterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def reduceStopwords(verse):
    
    stopWords = set(stopwords.words("english"))
    stopWords = stopWords.union(["ye","thou","thee","thy","thine"])
    reducedVerse = []
    for word in verse:
        if word not in stopWords:
            reducedVerse.append(word)
    return reducedVerse

def bibleToDict(filePath):
    # load bible txt file
    with open(f"{filePath}",mode="r",encoding="UTF-8") as bibleFile:
        bibleVerses = bibleFile.readlines()
        # lower and remove punctuation all bible verses
        table = str.maketrans('','',string.punctuation)

        bibleVerses = [ verse.lower().translate(table) for verse in bibleVerses]
        bibleVerses = [ reduceStopwords(word_tokenize(verse)[1:]) for verse in bibleVerses ]
        
        # lemmatize all bible verses 
        """
        for i,verse in enumerate(bibleVerses):
            bibleVerses[i] = [WordNetLemmatizer().lemmatize(word) for word in verse]
        """
        # poter stemming all bible verses
        
        for i,verse in enumerate(bibleVerses):
            bibleVerses[i] = [PorterStemmer().stem(word) for word in verse]
        
    # make word dict
    bibleWordDict = dict()
    for verse in bibleVerses:
        for word in verse:
            if word in bibleWordDict:
                bibleWordDict[word] += 1
            else:
                bibleWordDict[word] = 1
    return bibleWordDict
def equalizeDict(dict1,dict2):
    for wordNum in list(dict2.keys()):
        if wordNum not in dict1:
            dict1[wordNum] = 0
    for wordNum in list(dict1.keys()):
        if wordNum not in dict2:
            dict2[wordNum] = 0
    return dict1,dict2

