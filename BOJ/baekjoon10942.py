# 팰린드롬?
# https://www.acmicpc.net/problem/10942

from sys import stdin, setrecursionlimit

setrecursionlimit(2000)

def palindrome(start, end):
    if start > end:
        return 1
    elif dp[start][end] != -1:
        return dp[start][end]
    elif start == end:
        return 1
    else:
        dp[start][end] = palindrome(start+1, end-1) and (arr[start] == arr[end])
        return dp[start][end]

n = int(stdin.readline())
arr = [*map(int, stdin.readline().split())]
arr = [0] + arr

dp = [[-1] * (n+1) for _ in range(n+1)]

m = int(stdin.readline())
for _ in range(m):
    s, e = map(int, stdin.readline().split())

    if n != 1:
        print(1 if palindrome(s, e) else 0)
    else:
        print(1)
