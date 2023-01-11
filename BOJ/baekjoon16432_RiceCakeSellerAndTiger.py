# 떡장수와 호랑이
from sys import stdin

def dfs(prev_ricecake_type, days):
    if days == n:
        for a in answer: print(a)
        exit(0)

    for i in range(1, sell_schedule[days][0] + 1):
        ricecake_type = sell_schedule[days][i]

        if not visited[days][i] and (prev_ricecake_type != ricecake_type):
            visited[days][i] = True
            answer.append(ricecake_type)
            dfs(ricecake_type, days+1)
            answer.pop()

answer = list()

n = int(input())
sell_schedule = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(10)] for _ in range(1000)]

dfs(0, 0)

print(-1)
