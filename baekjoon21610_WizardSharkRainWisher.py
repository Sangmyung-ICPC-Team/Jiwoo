# 마법사 상어와 비바리기
from sys import stdin

def move_clouds(dir, dis):
    global clouds
    if dir == 1: unit_vector = (0, -1)
    elif dir == 2: unit_vector = (-1, -1)
    elif dir == 3: unit_vector = (-1, 0)
    elif dir == 4: unit_vector = (-1, 1)
    elif dir == 5: unit_vector = (0, 1)
    elif dir == 6: unit_vector = (1, 1)
    elif dir == 7: unit_vector = (1, 0)
    else: unit_vector = (1, -1)

    temp = clouds
    clouds = []
    for t in temp:
        x, y = t[0], t[1]
        for _ in range(dis):
            if (x+unit_vector[0]) == -1: x = n-1
            elif (x+unit_vector[0]) == n: x = 0
            else: x += unit_vector[0]

            if (y+unit_vector[1]) == -1: y = n-1
            elif (y+unit_vector[1]) == n: y = 0
            else: y += unit_vector[1]
        clouds.append((x, y))

def rain():
    for cloud in clouds:
        A[cloud[0]][cloud[1]] += 1

def remove_clouds():
    global clouds
    global removed
    removed = clouds
    # clouds = []

def copy_water():
    water_memo = []
    pos = [(-1, -1),
           (-1, 1),
           (1, -1),
           (1, 1)]

    for cloud in clouds:
        water_cnt = 0
        for p in pos:
            if (0 <= cloud[0]+p[0] < n) and (0 <= cloud[1]+p[1] < n):
                if A[cloud[0]+p[0]][cloud[1]+p[1]]:
                    water_cnt += 1
        water_memo.append((cloud[0], cloud[1], water_cnt))

    for memo in water_memo:
        A[memo[0]][memo[1]] += memo[2]

def gernerate_clouds():
    global clouds
    clouds = []
    for i in range(n):
        for j in range(n):
            if ((i, j) not in removed) and A[i][j] >= 2:
                A[i][j] -= 2
                clouds.append((i, j))

total_water = 0
n, m = map(int, input().split())
A = [list(map(int, stdin.readline().split())) for _ in range(n)]

removed = []
clouds = [(n-1, 0),
          (n-1, 1),
          (n-2, 0),
          (n-2, 1)]

for _ in range(m):
    d, s = map(int, input().split())
    move_clouds(d, s)
    rain()
    remove_clouds()
    copy_water()
    gernerate_clouds()

for i in range(n):
    for j in range(n):
        total_water += A[i][j]

print(total_water)
