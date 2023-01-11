# ATM
from sys import stdin

n = int(input())
p_wait = sorted(list(map(int, stdin.readline().split())))

min_wait = [0 for _ in range(n)]
min_wait[0] = p_wait[0]

for i in range(1, n):
    min_wait[i] = min_wait[i-1] + p_wait[i]

print(sum(min_wait))