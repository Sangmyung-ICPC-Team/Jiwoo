# 인접한 비트의 개수
from sys import stdin

def num_of_adjacent_bits(N, K):
    if n == 1:
        return 0

    dp = [[[0, 0] for _ in range(i)] for i in range(n + 1)]

    dp[1][0][0], dp[1][0][1] = 1, 1
    # print(sum(dp[1][0]))
    for i in range(2, n+1):
        for j in range(i):
            if j == i-1:
                dp[i][j] = [0, 1]
            else:
                dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]
                dp[i][j][1] = dp[i-1][j][0]
                if j - 1 >= 0:
                    dp[i][j][1] += dp[i-1][j-1][1]

    return sum(dp[N][K])

t = int(stdin.readline())

while t:
    n, k = map(int, stdin.readline().split())
    print(num_of_adjacent_bits(n, k))
    t -= 1
