###find the missing element in an array of size n (1 to n+1 elements)

from numpy import array
import numpy as np

def missing_ele(arr:array)->int:
    siz = np.max(arr)
    dummy = np.arange(siz+1)[1:]
    missing = np.sum(dummy) - np.sum(arr)

    return missing

a = [1,4,3,2,6]
print(missing_ele(a))