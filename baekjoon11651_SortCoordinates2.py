# 좌표 정렬하기2
n = int(input())
positions = [tuple(map(int, input().split())) for _ in range(n)]

positions.sort(key=lambda x: x[0])
positions.sort(key=lambda x: x[1])

for pos in positions:
    print(pos[0], pos[1])