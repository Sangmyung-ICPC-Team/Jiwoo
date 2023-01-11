# RGB거리
from sys import stdin
input = stdin.readline

n = int(int(input()))
costs = []

for _ in range(n):
    costs.append(list(map(int, input().split())))

dp = [[0, 0, 0] for _ in range(n)]
dp[0] = costs[0]

for i in range(1, n):
    for c in range(3):
        if c == 0:
            dp[i][c] = costs[i][c] + min(dp[i-1][1], dp[i-1][2])
        elif c == 1:
            dp[i][c] = costs[i][c] + min(dp[i-1][0], dp[i-1][2])
        else:
            dp[i][c] = costs[i][c] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[n-1]))