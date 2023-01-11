# 동전 0 (DP 안됨. Greedy로 풀어야 함)
n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)], reverse=True)

min_cnt = 0

while k:
    for coin in coins:
        min_cnt += k // coin
        k %= coin

print(min_cnt)