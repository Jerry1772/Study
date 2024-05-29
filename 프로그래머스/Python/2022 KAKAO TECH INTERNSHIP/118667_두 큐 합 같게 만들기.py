# https://school.programmers.co.kr/learn/courses/30/lessons/118667

def solution(queue1,queue2):
    queue = [*queue1, *queue2]
    left, right = 0, len(queue1)
    current, target = sum(queue1), sum(queue)
    iter = 0

    while left<right<len(queue):
        # print(current, target)
        if current*2 > target:
            left += 1
            current -= queue[left-1]
        elif current*2 < target:
            right += 1
            current += queue[right-1]
        else:
            return iter
        iter += 1
    return -1
            
if __name__ == "__main__":
    param = {
        "queue1": [1, 2, 1, 2],
		"queue2": [1, 10, 1, 2]
    }
    result = 7
    print(solution(**param), result)