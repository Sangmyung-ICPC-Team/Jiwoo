# 오큰수
from sys import stdin

n = int(input())
ans = [-1 for _ in range(n)]
seq = list(map(int, stdin.readline().split()))

stk = list()
curr_idx = 0

while curr_idx < n:
    if not stk:
        stk.append(curr_idx)
    else:
        if seq[stk[-1]] < seq[curr_idx]:
            ans[stk.pop()] = seq[curr_idx]
            continue
        else:
            stk.append(curr_idx)
    curr_idx += 1

print(*ans)