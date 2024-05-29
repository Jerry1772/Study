# https://school.programmers.co.kr/learn/courses/30/lessons/64064

import re
from itertools import product

def solution(user_id:list[str], banned_id:list[str]):
    answer = []

    ban_candidates = [[] for _ in range(len(banned_id))]
    for idx, _id in enumerate(banned_id):
        comp = re.compile(_id.replace("*","."))
        for user in user_id:
            if comp.fullmatch(user):
                ban_candidates[idx].append(user)
    
    for p in product(*ban_candidates):
        _set = frozenset(p)
        if len(_set) == len(ban_candidates):
            answer.append(_set)
    
    return len(set(answer))
        


if __name__ == "__main__":
    param = {
        "user_id": ["frodo", "fradi", "crodo", "abc123", "frodoc"],
		"banned_id": ["fr*d*", "*rodo", "******", "******"]
    }
    result = 3
    print(solution(**param), result)