# https://school.programmers.co.kr/learn/courses/30/lessons/150366

from typing import Union, List, Set


class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.val: Union[None, str] = None
        self.merged_with: Set[Cell] = set([])
        # cell 이 병합된 다른 셀의 정보를 가질 필요가 없음. manager가 병합정보와 해당 값을 dict에 가지고 있는게 맞는듯 한데, 일단 나중에 수정하는 걸로 미뤄둠

    def update(self, new_val):
        for cell in self.merged_with:
            cell.val = new_val
        self.val = new_val

    def add_merged_with(self, targets):
        self.merged_with.update(targets - {self})
        

class CellManager:
    def __init__(self):
        self.board = [[Cell(r, c) for c in range(51)] for r in range(51)]
        self.answer = []

    def update(self, r, c, value):
        r, c = int(r), int(c)
        self.board[r][c].update(value)

    def update_all(self, value1, value2):
        for row in self.board:
            for cell in row:
                if cell.val == value1:
                    cell.val = value2

    def merge(self, r1, c1, r2, c2):
        r1, r2, c1, c2 = list(map(int, [r1, r2, c1, c2]))
        if r1 == r2 and c1 == c2:
            return
        val = self.board[r1][c1].val or self.board[r2][c2].val
        merged_with = {self.board[r1][c1], self.board[r2][c2]}
        merged_with.update(self.board[r1][c1].merged_with)
        merged_with.update(self.board[r2][c2].merged_with)

        for cell in merged_with:
            cell.add_merged_with(merged_with)
            cell.val = val

    def unmerge(self, r, c):
        r, c = int(r), int(c)
        for cell in self.board[r][c].merged_with:
            cell.val = None
            cell.merged_with = set([])
        self.board[r][c].merged_with = set([])

    def print(self, r, c):
        r, c = int(r), int(c)
        val = self.board[r][c].val
        if val is None:
            self.answer.append("EMPTY")
        else:
            self.answer.append(val)


def solution(commands):
    manager = CellManager()
    for command in commands:
        command = command.split()
        if command[0] == 'UPDATE':
            if len(command) == 4:
                manager.update(*command[1:])
            else:
                manager.update_all(*command[1:])
        elif command[0] == "MERGE":
            manager.merge(*command[1:])
        elif command[0] == "UNMERGE":
            manager.unmerge(*command[1:])
        elif command[0] == "PRINT":
            manager.print(*command[1:])
    return manager.answer


if __name__ == "__main__":
    param = {
        "commands": ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
    }
    result = ["EMPTY", "group"]
    print(solution(**param), result)