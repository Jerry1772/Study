# https://school.programmers.co.kr/learn/courses/30/lessons/77486

def solution(enroll, referral, seller, amount):
    from math import ceil
    link, earn = {}, {i:0 for i in enroll}
    for i in range(len(enroll)):
        if referral[i]=='-': link[enroll[i]]='center'
        else: link[enroll[i]] = referral[i]
    for s, a in zip(seller,amount):
        m = 100*a
        while s!='center' and m>0:
            mm = ceil(m/10*9)
            earn[s]+=mm
            m-=mm
            s=link[s]
    return list(earn.values())

if __name__ == "__main__":
    param = {
        "enroll": ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        "referral": ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        "seller": ["young", "john", "tod", "emily", "mary"],
        "amount": [12, 4, 2, 5, 10]
    }

    result = [360, 958, 108, 0, 450, 18, 180, 1080]
    print(solution(**param), result)