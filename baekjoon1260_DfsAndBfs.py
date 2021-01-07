import sys
input = sys.stdin.readline

def DFS(s):
    visited.append(s)
    print(s, end=' ')
    for adj in range(1, n+1):
        if matrix[s][adj] and adj not in visited:
            DFS(adj)

def BFS(s):
    visited.append(s)
    q = [s]
    while q:
        curr = q.pop(0)
        print(curr, end=' ')
        for adj in range(1, n+1):
            # print(adj)
            if matrix[curr][adj] and adj not in visited:
                visited.append(adj)
                q.append(adj)

visited = []
n, m, v = map(int, input().split())
matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    matrix[v1][v2] = matrix[v2][v1] = 1

DFS(v)
print()
visited = []
BFS(v)