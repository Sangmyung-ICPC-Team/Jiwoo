# 가장 큰 정사각형
from sys import stdin

def get_the_biggest_square():
    dp = [[0 for _ in range(m)] for _ in range(n)]

    max_line = 0
    for i in range(0, n):
        for j in range(0, m):
            if i-1 < 0 or j-1 <0: # 테두리
                dp[i][j] = arr[i][j]
            elif arr[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
            max_line = max(max_line, dp[i][j])
    return max_line**2

n, m = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]

print(get_the_biggest_square())