# 센티와 마법의 뿅망치
from sys import stdin
import heapq

def make_short():
    cnt = 0
    while cnt < t:
        tallest, height = heapq.heappop(giant_heights)

        if height < h:
            return cnt
        elif height == 1:
            heapq.heappush(giant_heights, (-1, 1))
            return -1

        height //= 2
        heapq.heappush(giant_heights, (-height, height))

        cnt += 1

    tallest, height = giant_heights[0]

    if height < h:
        return cnt
    else:
        return -1

n, h, t = map(int, input().split())
giant_heights = []

for _ in range(n):
    height = int(stdin.readline().rstrip())
    heapq.heappush(giant_heights, (-height, height))

result = make_short()

if result > -1:
    print(f'YES\n{result}')
else:
    print(f'NO\n{heapq.heappop(giant_heights)[1]}')
