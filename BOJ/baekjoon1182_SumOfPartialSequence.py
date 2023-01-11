# 부분수열의 합
from sys import stdin

def dfs(curr_idx, curr_sum):
    if curr_idx == n:
        if curr_sum == s:
            global ans
            ans += 1
    elif curr_idx < n:
        dfs(curr_idx+1, curr_sum)
        dfs(curr_idx+1, curr_sum+seq[curr_idx])

n, s = map(int, input().split())
seq = list(map(int, stdin.readline().split()))
ans = 0

dfs(0, 0)

print(ans) if s != 0 else print(ans-1)
