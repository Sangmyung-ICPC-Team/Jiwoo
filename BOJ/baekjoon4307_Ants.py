# 개미
from sys import stdin

t = int(input())
answers = []

for _ in range(t):
    i, n = map(int, input().split())
    min_sec, max_sec = 0, 0
    for _ in range(n):
        loc = int(input())
        curr_min_sec = min(loc, i-loc)

        min_sec = max(min_sec, curr_min_sec)
        max_sec = max(max_sec, loc, i-loc)

    answers.append((min_sec, max_sec))

for answer in answers:
    print(*answer)