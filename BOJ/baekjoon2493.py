from collections import deque
from sys import stdin

n = int(stdin.readline())

if n == 1:
    print(0)
else:
    d = deque([*map(int, stdin.readline().split())])

    answer = list()
    front_tower = list()

    for i in range(1, n+1):
        curr = d.popleft()

        # front_tower[k][0]: 탑의 높이
        # front_tower[k][1]: 탑의 위치

        while front_tower and front_tower[-1][0] < curr:
            front_tower.pop()
        
        if not front_tower:
            answer.append(0)
        else:
            answer.append(front_tower[-1][1])

        front_tower.append((curr, i))

    print(*answer)
