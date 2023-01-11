# 최소 힙
import heapq
import sys
input = sys.stdin.readline

n = int(input())
min_heap = []
values = []

for _ in range(n):
    values.append(int(input()))

for v in values:
    if v == 0 and not min_heap:
        print(0)
    elif v == 0 and min_heap:
        print(heapq.heappop(min_heap))
    elif v != 0:
        heapq.heappush(min_heap, v)