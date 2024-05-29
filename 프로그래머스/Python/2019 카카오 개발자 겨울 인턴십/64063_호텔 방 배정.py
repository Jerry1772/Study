# https://school.programmers.co.kr/learn/courses/30/lessons/63063

import sys
sys.setrecursionlimit(10**6)

def find_parent(rooms, x):
    if x not in rooms:
        rooms[x] = x + 1
        return x

    rooms[x] = find_parent(rooms, rooms[x])
    return rooms[x]

def solution(k, room_number):
    rooms = {}
    answer = []

    for room in room_number:
        parent = find_parent(rooms, room)
        answer.append(parent)

    return answer


if __name__ == "__main__":
    param = {
        "k": 10,
		"room_number": [1,3,4,1,3,1]
    }
    result = [1,3,4,2,5,6]
    print(solution(**param), result)