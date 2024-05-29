# https://school.programmers.co.kr/learn/courses/30/lessons/12899


num = ['1','2','4']
def tkawls(n):
    if n<=3:
        return num[n-1]
    a,b = divmod(n-1,3)
    return tkawls(a)+num[b]

def solution(n):
    return tkawls(n)


if __name__ == "__main__":
    n, result = 4, 11
    print(solution(n), result)