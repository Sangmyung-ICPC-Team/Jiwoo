# 화장실의 규칙
import heapq
from sys import stdin
from collections import deque

n, m, k = map(int, stdin.readline().split())
lines = [deque() for _ in range(m)]
cnt = 0

# 사원 입력
for i in range(n):
    # i번째 사원은 i % m 줄에 서게 됨
    d, h = map(int, stdin.readline().split())
    line_num = i % m
    lines[line_num].append((-d, -h, line_num, i + 1))

rival = []
for i in range(m):
    if lines[i]:
        heapq.heappush(rival, lines[i].popleft())

while True:
    curr_turn = heapq.heappop(rival)
    if curr_turn[3] == k+1: # 데카의 차례
        break
    if lines[curr_turn[2]]:
        heapq.heappush(rival, lines[curr_turn[2]].popleft())
    cnt += 1

print(cnt)