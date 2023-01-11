# 토마토
from sys import stdin
from collections import deque

positions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():

    days = -1

    while ripe_tomato:
        days += 1
        for _ in range(len(ripe_tomato)):
            x, y = ripe_tomato.popleft()

            for pos in positions:
                nx = x + pos[0]
                ny = y + pos[1]
                if (0 <= nx < n) and (0 <= ny < m) and (box[nx][ny] == 0):
                    box[nx][ny] = 1
                    ripe_tomato.append((nx, ny))

    for b in box:
        if 0 in b: # 한줄 검사
            return -1
    return days

m, n = map(int, input().split())
box = []
ripe_tomato = deque()

for i in range(n):
    row = list(map(int, stdin.readline().split()))
    for j in range(m):
        if row[j] == 1:
            ripe_tomato.append((i, j))
    box.append(row)

print(bfs())
