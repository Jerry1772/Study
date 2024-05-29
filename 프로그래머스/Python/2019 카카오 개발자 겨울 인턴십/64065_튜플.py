# https://school.programmers.co.kr/learn/courses/30/lessons/64065
import re
from collections import Counter
def solution(s):
    rt = re.findall('[0-9]+', s)
    counter = Counter(rt)
    
    return list(map(int, sorted(counter.keys(), key=lambda x: counter[x], reverse=True)))

if __name__ == "__main__":
    param = {
        "s": "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    }
    result = [3,2,4,1]
    print(solution(**param), result)