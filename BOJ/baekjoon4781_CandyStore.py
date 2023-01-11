# 사탕 가게
from sys import stdin

def get_calorie(money):

    dp = [0]*(money + 1)

    for i in range(candies[0][1], money + 1):
        for cal, price in candies:
            if i - price >= 0:
                dp[i] = max(dp[i], cal + dp[i - price])

    return dp[money]

while True:
    n, m = map(float, stdin.readline().split())

    if n == 0 and m == 0.00:
        break

    m = int(m * 100 + 0.5)

    candies = list()
    for _ in range(int(n)):
        c, p = map(float, stdin.readline().split())
        candies.append((int(c), int(p * 100 + 0.5)))

    candies = sorted(candies, key = lambda x: x[1])

    print(get_calorie(m))
