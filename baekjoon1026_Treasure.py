# 보물
from sys import stdin

n = int(input())
a = sorted(list(map(int, stdin.readline().split())))
b = sorted(list(map(int, stdin.readline().split())), reverse=True)

s = 0
for i in range(n):
    s += a[i] * b[i]

print(s)