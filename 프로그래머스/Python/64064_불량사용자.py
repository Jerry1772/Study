# https://school.programmers.co.kr/learn/courses/30/lessons/64064

from itertools import product
import re
def solution(user_id, banned_id):
    answer = []
    len_ban = len(banned_id)
    possible_list = [[] for _ in range(len_ban)]
    for index, ban in enumerate(banned_id):
        comp = re.compile(ban.replace("*","."))
        for user in user_id:
            if comp.fullmatch(user):
                possible_list[index].append(user)


    for p in product(*possible_list):
        fset = frozenset(p)
        if len(fset) != len_ban :
            continue
        answer.append(fset)
    return len(set(answer))

if __name__ == "__main__":
    param = {
        "user_id": ["frodo", "fradi", "crodo", "abc123", "frodoc"],
		"banned_id": ["fr*d*", "*rodo", "******", "******"]
    }
    result = 3
    print(solution(**param), result)