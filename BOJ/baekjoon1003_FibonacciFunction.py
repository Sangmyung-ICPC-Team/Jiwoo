# 피보나치 함수
t = int(input())
arr = [int(input()) for _ in range(t)]

dp = [[1, 0], [0, 1]]
for i in range(2, max(arr)+1):
    dp.append([dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]])

for a in arr:
    print(dp[a][0], dp[a][1])