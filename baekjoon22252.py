from collections import defaultdict as dd
import sys
import heapq

input = sys.stdin.readline

gorillas = dd(list)

value = 0

q = int(input())
for _ in range(q):
    query = input().split(' ')

    name = query[1]
    if query[0] == '1':
        order = query[3:]
        for i in order:
            heapq.heappush(gorillas[name], int(i) * -1)
    else:
        cnt = int(query[2])
        for _ in range(cnt):
            if(not gorillas[name]):
                break;

            value += heapq.heappop(gorillas[name]) * -1

print(value)

