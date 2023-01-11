# 서울 지하철 2호선
from sys import stdin, setrecursionlimit
from collections import defaultdict, deque

setrecursionlimit(10000)

def find_cycle(start, curr, prev_cnt):
    if start == curr and prev_cnt >= 2:
        is_cycle[curr] = True
        return

    visited[curr] = True
    for adj in adj_list[curr]:
        if not visited[adj]:
            find_cycle(start, adj, prev_cnt+1)
        elif adj == start and prev_cnt >= 2: # cycle
            find_cycle(start, adj, prev_cnt)

def get_distances():
    dq = deque()

    for i in range(n):
        if is_cycle[i]:
            distance[i] = 0
            dq.append(i)

    while dq:
        curr = dq.popleft()

        for adj in adj_list[curr]:
            if distance[adj] == INF:
                dq.append(adj)
                distance[adj] = distance[curr] + 1

INF = 3000

n = int(input())
adj_list = defaultdict(list)
is_cycle = [False] * (n)
distance = [INF] * (n)

for _ in range(n):
    s1, s2 = map(int, stdin.readline().split())
    adj_list[s1-1].append(s2-1)
    adj_list[s2-1].append(s1-1)

for s in range(n):
    visited = [False]*(n)
    find_cycle(s, s, 0)

get_distances()

print(*distance)