# https://school.programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
    sumboard = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    n = len(sumboard)

    for s in skill:
        delta = ((-1)**s[0])*s[-1]
        sumboard[s[1]][s[2]] += delta
        sumboard[s[3]+1][s[4]+1] += delta
        sumboard[s[1]][s[4]+1] -= delta
        sumboard[s[3]+1][s[2]] -= delta
    for r in range(1, n):
        sumboard[r][0] = sumboard[r][0]+sumboard[r-1][0]
    for c in range(1, n):
        sumboard[0][c] = sumboard[0][c]+sumboard[0][c-1]
    for r in range(1, n):
        for c in range(1, n):
            sumboard[r][c] = sumboard[r][c]+sumboard[r-1][c]+sumboard[r][c-1]-sumboard[r-1][c-1]
    answer = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c]+sumboard[r][c]>0:
                answer += 1
    return answer

if __name__ == "__main__":
    board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
    result = 10
    print(solution(board, skill), result)