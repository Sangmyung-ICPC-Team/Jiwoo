# 항체 인식
from sys import stdin
from collections import deque

positions = [(0,1), (0,-1), (1,0), (-1,0)]

def bfs():
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    after_cnt = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and init[i][j] != after[i][j]:
                q.append((i, j))
                after_cnt += 1

                if after_cnt > 1:
                    return False

                while q:
                    curr_x, curr_y = q.popleft()
                    for x, y in positions:
                        r, c = curr_x+x, curr_y+y
                        if 0 <= r < n and 0 <= c < m:
                            if not visited[r][c] and init[curr_x][curr_y] == init[r][c] and after[curr_x][curr_y] == after[r][c]:
                                q.append((r, c))
                                visited[r][c] = True
                            elif not visited[r][c] and init[curr_x][curr_y] == init[r][c] and after[curr_x][curr_y] != after[r][c]:
                                return False

    return True

n, m = map(int, input().split())

init = []
after = []

for _ in range(n):
    init.append(list(map(int, stdin.readline().split())))

for _ in range(n):
    after.append(list(map(int, stdin.readline().split())))

print('YES' if bfs() else 'NO')