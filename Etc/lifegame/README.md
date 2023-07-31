Lifegame

# HOW TO RUN
1. edit config.json


- "sleep_time": 0.2,              ## generation 의 간격 (초 단위)
- "board_size": 20,               ## 좌,우 길이
- "point_x": [1, 2, 3, 4, 5],     ## 시작점의 x 좌표들
- "point_y": [1, 1, 1, 1, 1],     ## 시작점의 y 좌표들
- "print_iter": 1000,             ## 반복 횟수
- "alive_char": "*",              ## alive point들의 표시 형식
- "dead_char": " "                ## dead point 들의 표시 형식


2.  

- python => python main.py
- golang => go run main.go