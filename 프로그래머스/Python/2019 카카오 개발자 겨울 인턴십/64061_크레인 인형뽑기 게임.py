# https://school.programmers.co.kr/learn/courses/30/lessons/64061

import numpy as np

def solution(board, moves):
    board = np.array(board).T
    nonzero = board!=0
    
    basket = [-1]
    answer = 0

    for move in moves:
        move-=1
        if board[move].any():
            idx = nonzero[move].argmax()
            doll = board[move,idx]
            if basket[-1]==int(doll):
                answer += 2
                basket.pop()
            else:
                basket.append(doll)
            board[move,idx] = 0
            nonzero[move,idx] = 0

    return answer

if __name__ == "__main__":
    param = {
        "board": [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
		"moves": [1,5,3,5,1,2,1,4]
    }
    result = 4
    print(solution(**param), result)