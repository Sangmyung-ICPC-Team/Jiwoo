# 욕심쟁이 판다
from sys import stdin

positions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def free_panda(x, y):
    if dp[x][y]: return dp[x][y]

    dp[x][y] = 1
    for r, c in positions:
        if 0 <= x + r < n and 0 <= y + c < n:
            if forest[x + r][y + c] > forest[x][y]:
                dp[x][y] = max(dp[x][y], free_panda(x+r, y+c)+1)

    return dp[x][y]

n = int(input())
forest = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

result = 0

for i in range(n):
    for j in range(n):
        result = max(result, free_panda(i, j))

print(result)