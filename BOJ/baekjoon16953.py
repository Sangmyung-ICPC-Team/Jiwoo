# A -> B
# https://www.acmicpc.net/problem/16953

from collections import deque

INF = 1000
a, b = map(int, input().split())

q = deque([(a, 0)])
cnt = INF

while q:

    curr_n, curr_c = q.popleft()

    if curr_n == b:
        cnt = min(cnt, curr_c)
    else:
        if curr_n * 2 <= b:
            q.append((curr_n * 2, curr_c + 1))

        if int(str(curr_n) + '1') <= b:
            q.append((int(str(curr_n) + '1'), curr_c + 1))

print(-1 if cnt == INF else cnt + 1)
