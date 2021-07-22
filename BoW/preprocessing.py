# preprocessing bible verses
from nltk.stem import WordNetLemmatizer,PorterStemmer,LancasterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def reduceStopwords(verse):
    reducedVerse = []
    for word in verse:
        if word not in stopWords:
            reducedVerse.append(word)
    return reducedVerse

stopWords = set(stopwords.words("english"))

bibleVerses = []
# load bible txt file
with open("bible/KJV/Genesis.txt",mode="r",encoding="UTF-8") as bibleFile:
    bibleVerses = bibleFile.readlines()

# lower all bible verses
bibleVerses = [ verse.lower() for verse in bibleVerses]

bibleVerses = [ reduceStopwords(word_tokenize(verse)[1:]) for verse in bibleVerses ]

# lemmatize all bible verses 
for i,verse in enumerate(bibleVerses):
    bibleVerses[i] = [WordNetLemmatizer().lemmatize(word) for word in verse]
# print
for i in bibleVerses:
    print(i)

