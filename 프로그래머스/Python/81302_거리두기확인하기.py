# https://school.programmers.co.kr/learn/courses/30/lessons/81302

from itertools import combinations

def distance(r1, c1, r2, c2):
    man_d = abs(r1-r2)+abs(c1-c2)
    diag = False
    if man_d==2 and abs(r1-r2)==1:
        diag = True
    return man_d, diag
        
def check(places, r1, c1, r2, c2):
    dist, diag = distance(r1, c1, r2, c2)
    if dist > 2:
        return True
    if dist == 2:
        if not diag and places[(r1+r2)//2][(c1+c2)//2]=="X":
            return True
        if diag and places[r1][c2]==places[r2][c1]=="X":
            return True
    return False

def solution(places):
    return [1 if all([check(place, *p1, *p2) for p1, p2 in combinations([(r,c) for r, row in enumerate(place) for c, col in enumerate(row) if col=="P"], 2)]) else 0 for place in places]
    answer = []
    for place in places:
        participants = [(r,c) for r, row in enumerate(place) for c, col in enumerate(row) if col=="P"]
        result = [check(place, *p1, *p2) for p1, p2 in combinations(participants, 2)]
        answer.append(1 if all(result) else 0)
    
    return answer

if __name__ == "__main__":
    param = {
        "places": [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    }
    result = [1, 0, 1, 1, 1]
    print(solution(**param), result)