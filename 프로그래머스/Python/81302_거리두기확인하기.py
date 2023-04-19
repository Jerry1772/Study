# https://school.programmers.co.kr/learn/courses/30/lessons/81302

from itertools import combinations
def solution(places):
    answers = []
    for p in places:
        answer = 1
        p = [list(i) for i in p]
        person = []
        for r in range(5):
            for c in range(5):
                if p[r][c]=='P': person.append((r,c))
        cps = list(combinations(person,2))
        for cp in cps:
            r1,c1,r2,c2 = cp[0][0],cp[0][1],cp[1][0],cp[1][1]
            md = abs(r1-r2)+abs(c1-c2)
            if md>2: continue
            elif md==1: 
                answer=0
                break
            elif (md==2) and (r1==r2 or c1==c2):
                if p[(r1+r2)//2][(c1+c2)//2] != "X":
                    answer=0
                    break
            else:
                if not (p[r2][c1]==p[r1][c2]=='X'):
                    answer=0
                    break
        answers.append(answer)
    return answers

if __name__ == "__main__":
    param = {
        "places": [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    }
    result = [1,0,1,1,1]
    print(solution(**param), result)