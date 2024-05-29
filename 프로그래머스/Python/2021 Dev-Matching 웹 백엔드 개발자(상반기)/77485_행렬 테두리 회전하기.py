# https://school.programmers.co.kr/learn/courses/30/lessons/77485

from collections import deque
def solution(rows, columns, queries):
    mat = [[i+1 for i in range(columns*r, columns*(r+1))]for r in range(rows)]
    result = []
    for r1,c1,r2,c2 in queries:
        queue = deque([])
        for c in range(c1-1,c2):
            queue.append(mat[r1-1][c])
        for r in range(r1,r2):
            queue.append(mat[r][c2-1])
        for c in range(c2-2,c1-2,-1):
            queue.append(mat[r2-1][c])
        for r in range(r2-2,r1-1,-1):
            queue.append(mat[r][c1-1])
        result.append(min(queue))
        queue.appendleft(queue.pop())
        for c in range(c1-1,c2):
            mat[r1-1][c]=queue.popleft()
        for r in range(r1,r2):
            mat[r][c2-1]=queue.popleft()
        for c in range(c2-2,c1-2,-1):
            mat[r2-1][c]=queue.popleft()
        for r in range(r2-2,r1-1,-1):
            mat[r][c1-1]=queue.popleft()

    return(result)

if __name__ == "__main__":
    param = {
        "rows": 6,
		"columns": 6,
		"queries": [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
    }
    result = [8, 10, 25]
    print(solution(**param), result)