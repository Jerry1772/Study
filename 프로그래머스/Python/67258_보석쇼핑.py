# https://school.programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    #초기화
    endpoint = len(gems)
    contain_dict = {g:0 for g in gems}
    remain_kind = len(contain_dict.keys())
    
    contain_dict[gems[0]] = 1
    remain_kind -= 1
    
    i,j = 0,1
    answer = [i+1, j]
    length = float('inf')
    
    while i<j and j<=endpoint:
        if remain_kind == 0 and j-i < length:
            answer = [i+1,j]
            length = j-i
        if remain_kind > 0:
            if j == endpoint:
                break
            j += 1
            contain_dict[gems[j-1]] += 1
            if contain_dict[gems[j-1]] == 1:
                remain_kind -= 1
        else:
            i += 1
            contain_dict[gems[i-1]] -= 1
            if contain_dict[gems[i-1]] == 0:
                remain_kind += 1

    return answer
        
        
    

if __name__ == "__main__":
    param = {
        "gems": ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    }
    result = [3, 7]
    print(solution(**param), result)