# https://school.programmers.co.kr/learn/courses/30/lessons/150367

def check(dummy_parent:bool, binary:str):
    center = len(binary)//2
    root = binary[center]
    
    if center == 0: ## no more child => return True
        if dummy_parent and root == '1':
            return False
        return True

    if dummy_parent and root=='0': ## dummy parent and dummy child => recursive call
        return all([check(True, binary[:center]), check(True, binary[center+1:])])
    if dummy_parent and root=='1': ## dummy parent and non dummy child => return False
        return False

    if not dummy_parent and root=='0': ## non dummy parent and dummy child => recursive call
        return all([check(True, binary[:center]), check(True, binary[center+1:])])
    if not dummy_parent and root=='1':
        return all([check(False, binary[:center]), check(False, binary[center+1:])])

def solution(numbers):
    answer = []
    for n in numbers:
        b = bin(n)[2:]
        pow = 1
        while True:
            if (2**pow) -1 >= len(b) >= 2**(pow-1):
                b = "0"*((2**pow)-1 - len(b)) + b
                break
            pow += 1
        if b[len(b)//2] == "0":
            answer.append(False)
        else:
            answer.append(check(False, b))
    return list(map(int, answer))

if __name__ == "__main__":
    numbers = [7,42,5]
    result = [1,1,0]
    print(solution(numbers), result)