# 여러분의 다리가 되어드리겠습니다!
# https://www.acmicpc.net/problem/17352
from sys import stdin
from collections import defaultdict as dd

def dfs(start):

    s = list([start])

    while s:
        curr = s.pop()
        visited[curr] = True

        for adj in adj_list[curr]:
            if not visited[adj]:
                s.append(adj)

n = int(stdin.readline())
adj_list = dd(list)

for _ in range(n-2):
    v1, v2 = map(int, stdin.readline().split())

    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

visited = [False] * (n+1)

dfs(1)

for i in range(1, n+1):
    if not visited[i]:
        print(1, i)
        break
