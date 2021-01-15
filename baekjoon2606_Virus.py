# 바이러스
from sys import stdin
input = stdin.readline

def bfs():
    visited = [False for _ in range(n+1)]
    cnt = 0

    visited[1] = True
    q = [1]

    while q:
        curr = q.pop(0)
        for adj_comp in computers[curr]:
            if not visited[adj_comp]:
                cnt += 1
                visited[adj_comp] = True
                q.append(adj_comp)
    return cnt

n = int(input())
e = int(input())

computers = {}

for i in range(n):
    computers[i+1] = []

for _ in range(e):
    v1, v2 = map(int, input().split())
    computers[v1].append(v2)
    computers[v2].append(v1)

print(bfs())