# 최단경로
from sys import stdin
from collections import defaultdict
import heapq

INF = 200001

def get_shortest_path(start_node):
    visited = [False]*(vertex+1)
    distance = [INF]*(vertex+1)

    heap = [(0, start_node)]
    heapq.heapify(heap)
    distance[start_node] = 0

    while heap:
        w, node = heapq.heappop(heap)
        visited[node] = True
        for adj, weight in graph[node]:
            if not visited[adj] and distance[node] + weight < distance[adj]:
                distance[adj] = distance[node] + weight
                heapq.heappush(heap, (distance[adj], adj))

    for i in range(1, vertex+1):
        print(distance[i] if distance[i] != INF else 'INF')

vertex, edge = map(int, input().split())
k = int(input())

graph = defaultdict(list)
for _ in range(edge):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v, w))

get_shortest_path(k)