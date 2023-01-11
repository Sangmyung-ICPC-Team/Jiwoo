# 2×n 타일링 - bottom-up
n = int(input())

if n < 3:
    print(n)
else:
    dp = [0]*(n+1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

    print(dp[i])
