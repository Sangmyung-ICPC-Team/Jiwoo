# 숫자 카드 2

n = int(input())
arr = list(map(int, input().split()))
d = {}

for a in arr:
    if a in d:
       d[a] += 1
    else:
        d[a] = 1

m = int(input())
targets = list(map(int, input().split()))

for t in targets:
    if t in d:
        print(d[t], end=' ')
    else:
        print(0, end=' ')