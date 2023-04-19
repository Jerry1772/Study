# https://school.programmers.co.kr/learn/courses/30/lessons/150368

from numpy import array, dot
from itertools import product
def solution(users, emoticons):

    users = array(users)
    emoticons = array(emoticons)
    dc_ratio = product([10, 20, 30, 40], repeat=len(emoticons))
    
    max_membership = 0
    max_income = 0

    for dc in dc_ratio:
        membership = 0
        income = 0

        dc = array(dc)
        dc_to_float = (100-dc)/100
        
        emoticons_price = emoticons*dc_to_float
        for user in users:
            buy = user[0]<=dc
            cost = int(dot(emoticons_price, buy))
            if cost >= user[1]:
                membership += 1
            else:
                income += cost
        
        if (membership > max_membership) or (membership == max_membership and income > max_income):
            max_membership = membership
            max_income = income

    return [max_membership, max_income]

if __name__ == "__main__":
    users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
    emoticons = [1300, 1500, 1600, 4900]
    result = [4, 13860]
    print(solution(users, emoticons), result)