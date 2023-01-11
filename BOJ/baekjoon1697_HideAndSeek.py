INF = 100001
def hide_and_seek(start, des):
    visited = [False for _ in range(INF)]
    dp = [INF for _ in range(INF)]

    visited[start], dp[start] = True, 0

    q = [start]
    curr = start
    while curr != des:
        curr = q.pop(0)
        for adj in adjacent[curr]:
            if visited[adj] == False and dp[adj] > dp[curr] + 1:
                visited[adj] = True
                dp[adj] = dp[curr] + 1
                q.append(adj)

    return dp[des]


n, k = map(int, input().split())
adjacent = {}
for i in range(INF):
    adjacent[i] = []
    if i-1 >= 0:
        adjacent[i].append(i-1)
    if i+1 < INF:
        adjacent[i].append(i+1)
    if 2*i < INF:
        adjacent[i].append(2*i)

print(hide_and_seek(n, k))
