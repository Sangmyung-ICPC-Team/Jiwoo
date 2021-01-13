# 스택
from sys import stdin

n = int(stdin.readline())
s = []
o_result = []

for _ in range(n):
    comm = stdin.readline().strip().split(' ')

    if comm[0] == 'top':
        if s: o_result.append(s[-1])
        else: o_result.append(-1)
    elif comm[0] == 'pop':
        if s: o_result.append(s.pop())
        else: o_result.append(-1)
    elif comm[0] == 'size': o_result.append(len(s))
    elif comm[0] == 'empty':
        if s: o_result.append(0)
        else: o_result.append(1)
    else:  # push
        s.append(comm[1])

for o in o_result:
    print(o)