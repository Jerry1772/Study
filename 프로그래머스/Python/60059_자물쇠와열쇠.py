# https://school.programmers.co.kr/learn/courses/30/lessons/60059

def solution(key, lock):
    def rotation(key):
        return [list(i) for i in zip(*key[::-1])]

    def check(temp_lock):
        for i in range(len(key)-1, len(lock)-len(key)+1):
            for j in range(len(key)-1, len(lock)-len(key)+1):
                if temp_lock[i][j]!=1: return False
        return True
    t = [0 for _ in range(len(lock)+2*len(key)-2)]
    for _ in range(len(key)-1):
        lock.append(t[:])
        lock.insert(0, t[:])
    t = [0 for _ in range(len(key)-1)]
    for i in range(len(lock)):
        if len(lock[i])<len(lock[i-1]):
            lock[i]=t[:]+lock[i][:]+t[:]

    for _ in range(4):
        for i in range(len(lock)-len(key)+1):
            for j in range(len(lock)-len(key)+1):
                temp_lock = [lock[i][:] for i in range(len(lock))]
                for r in range(len(key)):
                    for c in range(len(key)):
                        temp_lock[i+r][j+c]+=key[r][c]
                if check(temp_lock): return True
        key = rotation(key)
    return False

if __name__ == "__main__":
    param = {
        "key": [[0, 0, 0], [1, 0, 0], [0, 1, 1]],
        "lock": [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    }
    result = True
    print(solution(**param), result)