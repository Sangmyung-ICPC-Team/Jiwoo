# 다리 놓기
from math import comb

t = int(input())
answers = []
for _ in range(t):
    n, m = map(int, input().split())
    answers.append(comb(m, n))

for a in answers:
    print(a)
