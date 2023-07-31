import time, os

class Board:

    def __init__(self, size:int):
        self.size = size
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.next_board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.__sleep_time = 2

    def print(self, count:int, true:str="1", false:str="0"):
        for i in range(count):
            
            os.system("cls")
            print(f"current count: {i+1}\n")
            
            for b in self.board:
                print(*[true if x==1 else false for x in b])

            self.__next_gen()
            time.sleep(self.__sleep_time)

    def update_sleep_time(self, aTime:int):
        self.__sleep_time = aTime

    def _get_neighbor(self, r:int, c:int):
        self.neighbor_count = 0
        for nr in [r-1,r,r+1]:
            if not(0<=nr<self.size):
                continue
            for nc in [c-1,c,c+1]:
                if not (0<=nc<self.size):
                    continue
                elif nr == r and nc == c:
                    continue
                if self.board[nr][nc] == 1:
                    self.neighbor_count += 1
        return self.neighbor_count
        
    def __next_gen(self):
        for r in range(self.size):
            for c in range(self.size):
                count = self._get_neighbor(r, c)
                if self.board[r][c] == 0 and count == 3:
                    self.next_board[r][c] = 1
                elif self.board[r][c] == 1 and count in (2,3):
                    self.next_board[r][c] = 1
                else:
                    self.next_board[r][c] = 0
        self.board = [l.copy() for l in self.next_board]

    def add_point(self, r:int, c:int):
        self.board[r][c] = 1
    
    def add_points(self, rs:list[int], cs:list[int]):
        if len(rs) != len(cs):
            exit("invalid point_x or point_y")
        for r,c in zip(rs, cs):
            self.add_point(r,c)