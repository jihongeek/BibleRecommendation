import numpy 
from preprocessing import equalizeDict,bibleToDict

def dictToRowVector(dict):
    dict = sorted(dict.items())
    rowVector = []
    for wordNum in dict:
        rowVector.append(wordNum[1])
    return numpy.array([rowVector])
def getCosineSimilarity(dict1,dict2):
    dict1,dict2 = equalizeDict(dict1,dict2)
    dict1,dict2 = dictToRowVector(dict1),dictToRowVector(dict2)
    return (numpy.inner(dict1,dict2)/(numpy.linalg.norm(dict1) * numpy.linalg.norm(dict2)))[0,0]

