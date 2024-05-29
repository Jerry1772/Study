# https://school.programmers.co.kr/learn/courses/30/lessons/92342

def solution(n, info):
    global answer, sol_result

    def score(ryan):
        s = 0
        for i in range(11):
            if ryan[i] == info[i] == 0:
                continue
            if ryan[i] > info[i]:
                s += 10 - i
            else:
                s -= 10 - i
        return s

    def dfs(idx, left, ryan):
        global answer, sol_result
        if idx == -1 and left:
            return
        if left == 0:
            s = score(ryan)
            if sol_result < s:
                answer = ryan[:]
                sol_result = s
            return
        for i in range(left, -1, -1):
            ryan[idx] = i
            dfs(idx-1, left-i, ryan)
            ryan[idx] = 0

    answer = [0 for _ in range(11)]
    sol_result = 0
    dfs(10, n, [0 for _ in range(11)])
    return answer if sol_result != 0 else [-1]

if __name__ == "__main__":
    n = 10
    info = [0,0,0,0,0,0,0,0,3,4,3]
    result = [1,1,1,1,1,1,1,1,0,0,2]
    print(solution(n, info), result)