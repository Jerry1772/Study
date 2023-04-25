# https://school.programmers.co.kr/learn/courses/30/lessons/161988
# 어떤 수열의 연속 부분 수열에 같은 길이의 펄스 수열을 각 원소끼리 곱하여 연속 펄스 부분 수열을 만들려 합니다. 
# 펄스 수열이란 [1, -1, 1, -1 …] 또는 [-1, 1, -1, 1 …] 과 같이 1 또는 -1로 시작하면서 1과 -1이 번갈아 나오는 수열입니다.
# 예를 들어 수열 [2, 3, -6, 1, 3, -1, 2, 4]의 연속 부분 수열 [3, -6, 1]에 펄스 수열 [1, -1, 1]을 곱하면 연속 펄스 부분수열은 [3, 6, 1]이 됩니다. 
# 또 다른 예시로 연속 부분 수열 [3, -1, 2, 4]에 펄스 수열 [-1, 1, -1, 1]을 곱하면 연속 펄스 부분수열은 [-3, -1, -2, 4]이 됩니다.
# 정수 수열 sequence가 매개변수로 주어질 때, 연속 펄스 부분 수열의 합 중 가장 큰 것을 return 하도록 solution 함수를 완성해주세요.

# 수열의 일부([n:m])합은 수열1 ([0:m])의 합 - 수열2 ([0:n-1])의 합으로 표현될 수 있으니까
# dp로 [0:i] 의 합을 i in range(len(seq)) 로 돌면서 계산해두고
# np.max - np.min 을 찾아내면 될듯
# 단, 펄스 수열은 2 가지 경우의 수가 생기므로 둘 다 고려해주어야 함
import numpy as np
def solution(sequence):
    pulse = np.array([(-1)**idx for idx in range(len(sequence))])
    
    seq = pulse*sequence
    
    dp = seq.cumsum()
    dp2 = dp*-1

    mx = np.max(dp) - min(np.min(dp), 0)
    mn = np.max(dp2) - min(np.min(dp2), 0)

    return int(max(mx, mn))

if __name__ == "__main__":
    param = {
        "sequence": [2, 3, -6, 1, 3, -1, 2, 4]
    }
    result = 10
    print(solution(**param), result)