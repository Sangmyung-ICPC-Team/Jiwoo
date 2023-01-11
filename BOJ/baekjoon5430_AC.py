# AC
import sys
input = sys.stdin.readline

def AC(m):
    is_reversed = False
    v = arrays[m]
    v = v[1:-2].split(',')
    for c in comm[m]:
        if c == 'R':
            is_reversed = not is_reversed
        elif c == 'D':
            if not v or v[0] == '':
                return 0
            if not is_reversed:
                v.pop(0)
            else:
                v.pop()

    if v:
        print('[', end='')
        if is_reversed:
            for k in range(len(v)-1, 0, -1):
                print(v[k], end=',')
            print('{}]'.format(v[0]))
        else:
            for k in range(len(v) - 1):
                print(v[k], end=',')
            print('{}]'.format(v[-1]))
    else:
        print('[]')

t = int(input())
comm = []
arrays = []

for _ in range(t):
    comm.append(input())
    n = int(input())
    arrays.append(input())

for i in range(t):
    if AC(i) == 0:
        print('error')
