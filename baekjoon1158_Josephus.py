# 요세푸스 문제
n, k = map(int, input().split())
seq = []

for i in range(1, n+1):
    seq.append(i)

if k == 1:
    print('<', end='')
    for i in range(n-1):
        print('{}, '.format(seq[i]), end='')
    print('{}>'.format(seq[-1]))
else:
    idx = 0
    o_result = '<'

    while len(seq) > 1:
        idx = (idx+k-1) % len(seq)
        o_result += str(seq.pop(idx)) + ', '

    o_result += str(seq[0]) + '>'
    print(o_result)