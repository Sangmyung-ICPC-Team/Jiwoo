# 숫자 할리갈리 게임
from sys import stdin
from collections import deque

def halli_galli(M):
    ground = [[], []]

    turn = 0
    while M:
        card = deque[turn].popleft()
        ground[turn].append(card)

        if not deque[turn]:
            return turn ^ 1 # 상대방의 승리

        if ground[0] and ground[1] and ground[0][-1] + ground[1][-1] == 5:
            deque[1].extend(ground[0]+ground[1])
            ground = [[], []]

        if card == 5:
            if ground[1]:
                deque[0].extend(ground[1])
            if ground[0]:
                deque[0].extend(ground[0])
            ground = [[], []]

        M -= 1
        turn ^= 1

    if len(deque[0]) > len(deque[1]): return 0
    elif len(deque[0]) < len(deque[1]): return 1
    else: return -1

n, m = map(int, input().split())
deque = [deque(), deque()]

for _ in range(n):
    do, su = map(int, stdin.readline().split())
    deque[0].appendleft(do)
    deque[1].appendleft(su)

result = halli_galli(m)

if result == 0: # 도도 승
    print('do')
elif result == 1: # 수연 승
    print('su')
else: # 비김
    print('dosu')
