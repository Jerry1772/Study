# https://school.programmers.co.kr/learn/courses/30/lessons/67257

from copy import deepcopy
from itertools import permutations
from re import split as sp

def solution(ex):
    value = 0
    ex = sp(r'(\D)',ex)
    operation = [i for i in ['-','+','*'] if i in ex]
    operation = list(permutations(operation))
    for ops in operation:
        temp = deepcopy(ex)
        for op in ops:
            while op in temp:
                ind = temp.index(op)
                temp [ind] = str(eval(temp[ind-1]+temp[ind]+temp[ind+1]))
                temp = temp[:ind-1]+[temp[ind]]+temp[ind+2:]            
            
        value = max(abs(int(temp[0])),value)
    return(value)

if __name__ == "__main__":
    param = {
        "ex": "100-200*300-500+20"
    }
    result = 60420
    print(solution(**param), result)