# 가장 긴 증가하는 부부 수열
from sys import stdin

def get_logest_seq():
    dp[0] = 1
    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j])
        dp[i] += 1
    return max(dp)

n = int(input())
a = list(map(int, stdin.readline().split()))

dp = [0]*n

print(get_logest_seq())