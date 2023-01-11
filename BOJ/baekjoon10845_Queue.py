# 큐
from sys import stdin

n = int(stdin.readline())
q = []
o_result = []

for _ in range(n):
    comm = stdin.readline().strip().split()

    if comm[0] == 'pop':
        if q: o_result.append(q.pop(0))
        else: o_result.append(-1)
    elif comm[0] == 'size':
        o_result.append(len(q))
    elif comm[0] == 'empty':
        if q: o_result.append(0)
        else: o_result.append(1)
    elif comm[0] == 'front':
        if q: o_result.append(q[0])
        else: o_result.append(-1)
    elif comm[0] == 'back':
        if q: o_result.append(q[-1])
        else: o_result.append(-1)
    else:  # push
        q.append(comm[1])

for o in o_result:
    print(o)