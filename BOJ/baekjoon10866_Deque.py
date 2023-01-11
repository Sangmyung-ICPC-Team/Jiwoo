# 덱
from sys import stdin
from collections import deque

n = int(input())
d = deque()
o_result = []

for _ in range(n):
    comm = stdin.readline().split()

    if comm[0] == 'push_back':
        d.append(comm[1])
    elif comm[0] == 'push_front':
        d.appendleft(comm[1])
    elif comm[0] == 'front':
        if d:
            o_result.append(d[0])
        else:
            o_result.append(-1)
    elif comm[0] == 'back':
        if d:
            o_result.append(d[-1])
        else:
            o_result.append(-1)
    elif comm[0] == 'size':
        o_result.append(len(d))
    elif comm[0] == 'empty':
        if d:
            o_result.append(0)
        else:
            o_result.append(1)
    elif comm[0] == 'pop_front':
        if d:
            o_result.append(d.popleft())
        else:
            o_result.append(-1)
    else:
        if d:
            o_result.append(d.pop())
        else:
            o_result.append(-1)

for o in o_result:
    print(o)