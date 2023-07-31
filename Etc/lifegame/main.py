
# 이웃의 수가 2,3이면 그대로
# 이웃의 수가 3이면 부활 가능
# 이웃의 수가 1이하, 4이상이면 사라짐
from board import Board
from config import Config
import os
__location__ = os.path.realpath(
                 os.path.join(
                   os.getcwd(), 
                   os.path.dirname(__file__)
                 )
               )

if __name__ == "__main__":

    sConfig = Config.from_path(os.path.join(__location__, 'config.json'))

    b = Board(sConfig.board_size)
    b.add_points(sConfig.point_x, sConfig.point_y)
    b.update_sleep_time(sConfig.sleep_time)
    b.print(count=sConfig.print_iter, 
            true=sConfig.char_alive, 
            false=sConfig.char_dead)