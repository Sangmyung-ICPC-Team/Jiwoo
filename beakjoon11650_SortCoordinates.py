# 좌표 정렬하기
from sys import stdin

n = int(input())
positions = []

for _ in range(n):
    positions.append(list(map(int, stdin.readline().split())))

positions.sort(key=lambda x: x[1])
positions.sort(key=lambda x: x[0])

for i in range(n):
    print(positions[i][0], positions[i][1])