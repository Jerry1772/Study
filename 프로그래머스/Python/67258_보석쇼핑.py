# https://school.programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    max_length = len(gems)
    gem_count = {gem:0 for gem in gems}
    remains = len(gem_count.keys())

    min_length = len(gem_count.keys())-1
    optimal = 2*len(gems)
    left, right = 1, 1
    answer = [1, 1]

    gem_count[gems[0]] += 1
    remains -= 1

    while left<=right:
        print(f"left: {left}, right: {right}, remains: {remains}, gem_count: {gem_count}, gems: {gems[left-1:right]}")
        if remains == 0:
            if right-left+1 < optimal:
                optimal = right-left+1
                answer = [left, right]
            gem_count[gems[left-1]] -= 1
            if not gem_count[gems[left-1]]:
                remains += 1
            left += 1
            if optimal == min_length:
                return answer
        else:
            if right+1 > max_length:
                return answer
            if gem_count[gems[right]] == 0:
                remains -= 1
            gem_count[gems[right]] += 1
            right += 1

    return answer
            
            
                
                

if __name__ == "__main__":
    param = {
        "gems": 	["AA", "AB", "AC", "AA", "AC"]
    }
    result = [1, 3]
    print(solution(**param), result)