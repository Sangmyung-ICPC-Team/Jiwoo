# 수들의 합
s = int(input())
n, total = 0, 0
while True:
    if total > s:
        break
    n += 1
    total += n

print(n-1)