# 사탕 줍기 대회
from sys import stdin

def one_line_max(arr, length):
    if length < 3:
        return max(arr)

    dp = [0]*length
    dp[0], dp[1] = arr[0], max(arr[0], arr[1])

    for i in range(2, length):
        dp[i] = max(dp[i-2] + arr[i], dp[i-1])

    return dp[-1]


while True:
    m, n = map(int, stdin.readline().split())

    if m == 0 and n == 0:
        break

    line_max = list()

    for i in range(m):
        line = list(map(int, stdin.readline().split()))
        line_max.append(one_line_max(line, n))

    print(one_line_max(line_max, m))