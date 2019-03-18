from functools import reduce
from typing import Union
import operator

def getFromDict(dataDict: dict, mapList:list)->Union[str,int]:
    value = None
    """
        data = {'a': {'r': 1, 's': 2, 't': 3}
        getFromDict(data,['a','s'])
        output: 2

    """
    try:
        value=reduce(operator.getitem, mapList, dataDict)
    except KeyError:
        pass
    finally:
        return value
