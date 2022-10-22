###find a pair with the given sum in an array
from numpy import array
import numpy as np

def find_pair(arr:array, target:int)->list:
    li = list(arr)
    tu = list()
    cons = list()
    for i in (li):
        if i not in tu:
            rem = target- i
            if rem in li:
                tu.append(i)
                tu.append(rem)

    return tu

input= np.array([8,7,2,5,3,1])
print(find_pair(input, 10))



