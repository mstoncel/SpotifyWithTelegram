from functools import reduce
import operator

def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)
