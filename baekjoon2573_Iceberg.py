# 빙산
from sys import stdin

def dfs(row, col):
    stack = list()
    stack.append((row, col))
    while stack:
        curr_pos = stack.pop()
        visited[curr_pos[0]][curr_pos[1]] = True

        position = [(curr_pos[0]-1, curr_pos[1]),
                    (curr_pos[0]+1, curr_pos[1]),
                    (curr_pos[0], curr_pos[1]-1),
                    (curr_pos[0], curr_pos[1]+1)]

        for pos in position:
            if ice_land[pos[0]][pos[1]] and (not visited[pos[0]][pos[1]]):
                stack.append((pos[0], pos[1]))

def count_iceberg():
    land = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if ice_land[i][j] and (not visited[i][j]):
                land += 1
                dfs(i, j)
            if land > 1:
                return land
    return land

def melt():
    melt_memo = list()

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            melt_cnt = 0

            if not ice_land[i - 1][j]:
                melt_cnt += 1
            if not ice_land[i + 1][j]:
                melt_cnt += 1
            if not ice_land[i][j - 1]:
                melt_cnt += 1
            if not ice_land[i][j + 1]:
                melt_cnt += 1

            if melt_cnt:
                melt_memo.append((i, j, melt_cnt))

    for memo in melt_memo:
        ice_land[memo[0]][memo[1]] -= memo[2]

        if ice_land[memo[0]][memo[1]] < 0:
            ice_land[memo[0]][memo[1]] = 0

n, m = map(int, stdin.readline().split())
ice_land = [list(map(int, stdin.readline().split())) for _ in range(n)]

curr_land = 1
years = 0

while curr_land == 1:
    visited = [[False for _ in range(m)] for _ in range(n)]
    years += 1
    melt()
    curr_land = count_iceberg()

print(0) if curr_land == 0 else print(years)