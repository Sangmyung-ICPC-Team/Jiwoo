# 이친수

n = int(input())

if n < 3:
    print(1)
else:
    dp = [0 for _ in range(n + 1)]
    dp[1], dp[2] = 1, 1

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n])