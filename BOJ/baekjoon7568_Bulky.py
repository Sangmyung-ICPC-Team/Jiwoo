# 덩치
from sys import stdin

n = int(input())
bulkys = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

for curr_b in bulkys:
    rank = 1
    for comp_b in bulkys:
        if curr_b[0] < comp_b[0] and curr_b[1] < comp_b[1]:
            rank += 1
    print(rank, end=' ')