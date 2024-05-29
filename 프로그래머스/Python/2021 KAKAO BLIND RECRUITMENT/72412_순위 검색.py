# https://school.programmers.co.kr/learn/courses/30/lessons/72412

import bisect

def solution(info, query):
    L = ['java','python','cpp']
    J = ['backend','frontend']
    C = ['junior','senior']
    F = ['chicken','pizza']
    answer = []
    dic = {}
    cache = {}
    for l in L: 
        dic[l]={}
        for j in J:
            dic[l][j]={}
            for c in C:
                dic[l][j][c]={}
                for f in F:
                    dic[l][j][c][f]=[]

    for i in info:
        i = list(i.split())
        dic[i[0]][i[1]][i[2]][i[3]].append(int(i[4]))
        dic[i[0]][i[1]][i[2]][i[3]].sort()

    for q in query:
        l,j,c,f,s = list(q.replace(' and','').split())
        count = 0
        if q in cache:
            count = cache[q]
        else:
            l=L if l=='-' else [l]
            j=J if j=='-' else [j]
            c=C if c=='-' else [c]
            f=F if f=='-' else [f]
            s = int(s)
            for ll in l:
                for jj in j:
                    for cc in c:
                        for ff in f:
                            count+=len(dic[ll][jj][cc][ff])-bisect.bisect_left(dic[ll][jj][cc][ff],s)
            cache[q] = count
        answer.append(count)

    return(answer)


if __name__ == "__main__":
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    result = [1,1,1,1,2,4]
    print(solution(info, query), result)