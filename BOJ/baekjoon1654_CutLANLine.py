# 랜선 자르기
from sys import stdin

k, n = map(int, input().split())
lan_lengths = [int(stdin.readline()) for _ in range(k)]

start, end = 1, max(lan_lengths)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for lan in lan_lengths:
        total += lan // mid

    if total < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
