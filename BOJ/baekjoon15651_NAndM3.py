# N과 M (3)
def dfs(length):
    if length == m:
        print(*selected)
    else:
        for i in range(1, n+1):
            selected.append(i)
            dfs(length+1)
            selected.pop()

n, m = map(int, input().split())
selected = list()

dfs(0)