n = 3
nums = [1,5,3]
op_nums = [1,1,0]

from itertools import permutations
operators = []
cache = {}
for cnt, op in zip(op_nums, ("+","-","*")):
    operators.extend([op]*cnt)

init_num = nums[0]
nums = nums[1:]
min_val = float("inf")
max_val = -float("inf")

for p in permutations(operators, n-1):
    num = init_num
    if p in cache:
        continue
    
    for n, o in zip(nums, p):
        num = eval(f"{num}{o}{n}")
    
    min_val = min(num, min_val)
    max_val = max(num, max_val)
print(min_val, max_val)


#아래는 좋은 예시
# import sys

# input = sys.stdin.readline
# N = int(input())
# num = list(map(int, input().split()))
# op = list(map(int, input().split()))

# maximum = -1e9
# minimum = 1e9

# cache = {}

# def dfs(depth, total, plus, minus, multiply):
#     global maximum, minimum

#     if depth == N:
#         maximum = max(total, maximum)
#         minimum = min(total, minimum)
#         return

#     if plus:
#         dfs(depth + 1, total + num[depth], plus - 1, minus, multiply)
#     if minus:
#         dfs(depth + 1, total - num[depth], plus, minus - 1, multiply)
#     if multiply:
#         dfs(depth + 1, total * num[depth], plus, minus, multiply - 1)

# dfs(1, num[0], op[0], op[1], op[2])
# print(minimum, maximum)