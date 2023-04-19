# https://school.programmers.co.kr/learn/courses/30/lessons/42895

def solution(n, number):
    # n == 1일 경우 그냥 리턴
    if number == n:
        return 1
    
    # 각 사용횟수별로 만들어낼 수 있는 모든 경우의 수를 포함
    possibilities = {i: {int(str(n) * i)} for i in range(1, 9)}

    # 특정 수를 만들어내기 위한 최소 횟수를 기록
    min_uses = {num: 1 for num in possibilities[1]}

    # 2부터 8까지 모든 경우의 수에 대해 계산
    for i in range(2, 9):
        for j in range(1, i):
            for left in possibilities[j]:
                for right in possibilities[i - j]:
                    possibilities[i].add(left + right)
                    possibilities[i].add(left - right)
                    possibilities[i].add(left * right)
                    if right != 0:
                        possibilities[i].add(left // right)

        # number 가 나왔는지 확인
        if number in possibilities[i]:
            return i

        # 최소 횟수 갱신
        for num in possibilities[i]:
            if num not in min_uses:
                min_uses[num] = i

    # 답 안나오면 -1 리턴
    return -1

if __name__ == "__main__":
    n, number, result = 5, 12, 4
    print(solution(n, number), result)