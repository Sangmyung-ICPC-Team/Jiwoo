# 정수 삼각형
from sys import stdin

n = int(input())
triangle = [[*map(int, stdin.readline().split())] for _ in range(n)]
dp = [[] for _ in range(n)]

dp[0].append(triangle[0][0])

for level in range(1, n):
    for v in range(level+1):
        if v == 0:
            dp[level].append(triangle[level][v] + dp[level-1][v])
        elif v == level:
            dp[level].append(triangle[level][v] + dp[level-1][v-1])
        else:
            dp[level].append(triangle[level][v] + max(dp[level-1][v-1], dp[level-1][v]))

print(max(dp[n-1]))