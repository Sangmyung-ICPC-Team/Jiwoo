def Sum123(n):
    for i in range(4, n+1):
        dp.append(dp[i-3] + dp[i-2] + dp[i-1])

t = int(input())
arr = []

for _ in range(t):
    arr.append(int(input()))

dp = [0, 1, 2, 4]
Sum123(max(arr))

for v in arr:
    print(dp[v])