# N과 M (4)
def dfs(curr, length):
    if length == m:
        print(*selected)
    else:
        for i in range(curr, n+1):
            selected.append(i)
            dfs(i, length+1)
            selected.pop()

n, m = map(int, input().split())
selected = list()

dfs(1, 0)