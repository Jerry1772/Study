# https://school.programmers.co.kr/learn/courses/30/lessons/150369

def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups:
        capacity = cap
        
        for target in (deliveries, pickups):
            try:
                while target[-1] == 0:
                    target.pop(-1)
                    if not target:
                        break
            except IndexError: pass
     
        
        answer += 2*(max(len(deliveries), len(pickups)))
        
        while capacity and any(deliveries):
            if deliveries[-1] > capacity:
                deliveries[-1] -= capacity
                capacity = 0
            else:
                capacity -= deliveries.pop(-1)
        
        capacity = 0

        while capacity < cap and any(pickups):
            if pickups[-1] > (cap-capacity):
                pickups[-1] -= (cap-capacity)
                capacity = cap
            else:
                capacity += pickups.pop(-1)
        
    return answer

if __name__ == "__main__":
    cap = 2
    n = 7
    deliveries = [1,0,2,0,1,0,2]
    pickups = [0,2,0,1,0,2,0]
    result = 30
    print(solution(cap, n, deliveries, pickups), result)