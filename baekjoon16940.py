# BFS 스페셜 저지
# https://www.acmicpc.net/problem/16940
from sys import stdin
from collections import defaultdict as dd, deque

n = int(stdin.readline())

adjList = dd(list)

for i in range(n-1):
    v1, v2 = map(int, stdin.readline().split())
    adjList[v1].append(v2)
    adjList[v2].append(v1)

order = [*map(int, stdin.readline().split())]

if order[0] != 1:
    print(0)
else:

    # 입력된 순서대로 우선순위를 지정
    priorities = [0] * (n + 1)
    for i in range(n):
        priorities[order[i]] = i + 1

    # 우선순위를 바탕으로 인접리스트 정렬
    for i in range(1, n+1):
        adjList[i].sort(key = lambda x : priorities[x])

    visited = [False] * (n+1)
    visited[1] = True

    q = deque([1])
    answer = list()

    while q:
        curr = q.popleft()
        answer.append(curr)

        for adj in adjList[curr]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True

    print(1 if answer == order else 0)
