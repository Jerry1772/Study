# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    dic = {}
    for n in nums:
        try: dic[n]+=1
        except: dic[n]=1
    return min(len(dic),len(nums)//2)

if __name__ == "__main__":
    nums = [3,3,3,2,2,4]
    result = 3
    print(solution(nums), result)