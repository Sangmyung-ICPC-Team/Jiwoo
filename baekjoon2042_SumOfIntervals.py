# 구간 합 구하기
from sys import stdin

def init(s, e, node):
    if s == e:
        tree[node] = arr[s]
        return tree[node]
    mid = (s+e)//2
    tree[node] = init(s, mid, node*2) + init(mid+1, e, node*2+1)
    return tree[node]

def sumOfIntervals(s, e, node, left, right):
    if left > e or right < s: # 범위에서 벗어남
        return 0
    if left <= s and e <= right:
        return tree[node]

    mid = (s+e)//2
    return sumOfIntervals(s, mid, node*2, left, right) + \
           sumOfIntervals(mid+1, e, node*2+1, left, right)

def update(s, e, node, idx, dif):
    if idx < s or idx > e:
        return

    tree[node] += dif
    if s == e:
        return
    mid = (s+e)//2
    update(s, mid, node*2, idx, dif)
    update(mid+1, e, node*2+1, idx, dif)

n, m, k = map(int, input().split())
arr = [int(stdin.readline()) for _ in range(n)]
commands = [list(map(int, stdin.readline().split())) for _ in range(m+k)]
tree = [0]*(n*4)

init(0, n-1, 1)

for cmd in commands:
    if cmd[0] == 1:
        dif = cmd[2] - arr[cmd[1]-1]
        update(0, n-1, 1, cmd[1]-1, dif)
        arr[cmd[1]-1] = cmd[2]
    else:
        print(sumOfIntervals(0, n-1, 1, cmd[1]-1, cmd[2]-1))