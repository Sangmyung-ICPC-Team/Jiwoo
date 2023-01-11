# 스타트와 링크
from sys import stdin

def get_team_capa(team):
    total_capa = 0

    for i in range(n//2-1):
        for j in range(i+1, n//2):
            total_capa += capabilities[team[i]][team[j]] + capabilities[team[j]][team[i]]

    return total_capa

def make_team(curr_emp, cnt):
    if cnt == n/2:
        global min_gap
        global start
        global link

        for e in range(n):
            if selected[e] == True: # start 팀
                start.append(e)
            else: # link 팀
                link.append(e)

        start_capa = get_team_capa(start)
        link_capa = get_team_capa(link)

        min_gap = min(min_gap, abs(start_capa-link_capa))

        start = []
        link = []
    else:
        for i in range(curr_emp, n):
            if not selected[i]:
                selected[i] = True
                make_team(i+1, cnt+1)
                selected[i] = False

min_gap = 10000
start, link = [], []

n = int(input())
selected = [False for _ in range(n)]
capabilities = [[*map(int, stdin.readline().split())] for _ in range(n)]

make_team(0, 0)
print(min_gap)