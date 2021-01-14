# 단지번호붙이기
def dfs(r, c):
    if r >= 0 and c >= 0:
        visited[r][c] = True

        adj_num = 0
        adjacents = [
            (r-1, c),
            (r+1, c),
            (r, c-1),
            (r, c+1)
        ]

        for adj in adjacents:
            if 0 <= adj[0] < n and 0 <= adj[1] < n:
                if comp[adj[0]][adj[1]] and not visited[adj[0]][adj[1]]:
                    adj_num += dfs(adj[0], adj[1])
        return 1 + adj_num

    else: return 0

def numbering():
    cnt = 0
    comp_numbers = []

    for i in range(n):
        for j in range(n):
            if comp[i][j] and not visited[i][j]:
                cnt += 1
                comp_numbers.append(dfs(i, j))

    comp_numbers.sort()
    print(cnt)
    for c_n in comp_numbers:
        print(c_n)

n = int(input())
comp = []
visited = [[False for _ in range(n)] for _ in range(n)]

for _ in range(n):
    comp.append(list(map(int, input())))

numbering()