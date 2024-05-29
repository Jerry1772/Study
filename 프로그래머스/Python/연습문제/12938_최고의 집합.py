# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    common = s//n
    if common == 0:
        return [-1]
    answer = [(common)+1 for _ in range(s%n)]
    while len(answer)!= n:
        answer.append(common)
    return answer[::-1]

if __name__ == "__main__":
    param = {
        "n": 2,
		"s": 9
    }
    result = [4, 5]
    print(solution(**param), result)