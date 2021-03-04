n = int(input())
wine = [int(input()) for _ in range(n)] 

if n < 3:
    print(sum(wine))
else:
    dp = [0 for _ in range(n)]
    dp[0], dp[1] = wine[0], wine[0] + wine[1]
    dp[2] = max(wine[0]+wine[2], wine[1]+wine[2], wine[0]+wine[1]) 

    for i in range(3, n):
        dp[i] = max(dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i], dp[i-1]) 

    print(dp[n-1])