# 학교 탐방하기
from sys import stdin
from collections import defaultdict
import heapq

def prim(heap, start_node, flag):
    visited = [False for _ in range(n + 1)]

    fatigue = 0

    visited[0] = True

    while heap:
        hill, adj = heapq.heappop(heap)
        if not visited[adj]:
            visited[adj] = True
            fatigue += hill

            for i in adj_list[adj]:
                if not visited[i[1]]:
                    heapq.heappush(heap, (i[0]*flag, i[1]))

    return fatigue

n, m = map(int, input().split())
adj_list = defaultdict(list)

for _ in range(m+1):
    a, b, c = map(int, stdin.readline().split())
    adj_list[a].append((c^1, b)) # XOR 연산
    adj_list[b].append((c^1, a)) # XOR 연산

list_for_worst = [(-c, adj) for c, adj in adj_list[0]]
best = prim(adj_list[0], 0, 1) # 최소힙 사용
worst = prim(list_for_worst, 0, -1) # 최대힙 사용

print(worst**2 - best**2)