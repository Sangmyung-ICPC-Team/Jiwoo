# 소수 찾기
from sys import stdin

n = int(input())
arr = [*map(int, stdin.readline().split())]

memo = {2: True, 3: True}
cnt = 0

for a in arr:
    if a != 2 and a % 2 == 0:
        continue
    else:
        if a == 1:
            continue
        if a in memo:
            cnt += 1
            continue
        else:
            for i in range(3, a):
                if a % i == 0:
                    break
                elif i == a-1:
                    memo[i] = True
                    cnt += 1

print(cnt)