# 대칭 차집합
from sys import stdin

n_a, n_b = map(int, stdin.readline().split())
a = stdin.readline().split()
b = stdin.readline().split()

s_d = {}

for e in a+b:
    if e in s_d:
        del s_d[e]
    else:
        s_d[e] = 1

print(len(s_d))