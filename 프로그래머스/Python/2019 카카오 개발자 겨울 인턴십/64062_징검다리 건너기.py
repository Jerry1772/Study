# https://school.programmers.co.kr/learn/courses/30/lessons/64062

def count_zeros(stones, mid, k):
    consecutive_zeros = 0

    for stone in stones:
        if stone < mid:
            consecutive_zeros += 1
            if consecutive_zeros >= k:
                return True
        else:
            consecutive_zeros = 0

    return False

def solution(stones, k):
    left = 1
    right = 200000000

    while left <= right:
        mid = (left + right) // 2
        found = count_zeros(stones, mid, k)

        if found:
            right = mid - 1
        else:
            left = mid + 1

    return right



if __name__ == "__main__":
    param = {
        "stones": [2, 4, 5, 3, 2, 1, 4, 2, 5, 1],
		"k": 3
    }
    result = 3
    print(solution(**param), result)