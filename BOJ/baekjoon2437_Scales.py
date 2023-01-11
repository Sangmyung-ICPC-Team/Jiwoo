# 저울
from sys import stdin

n = int(input())
weights = sorted(list(map(int, stdin.readline().split())))

measurable = 0
for w in weights:
    if w <= measurable+1:
        measurable += w
    else: break
print(measurable+1)
