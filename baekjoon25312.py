from sys import stdin
import heapq


def getGCD(a, b):

    a, b = max(a, b), min(a, b)

    while (a % b) != 0:
        a, b = b, a % b

    return b


n, m = map(int, stdin.readline().split())
heap = []

for _ in range(n):
    w, v = map(int, stdin.readline().split())
    heapq.heappush(heap, (-v/w, w, v))

nume = 1 # 분모
denomi= 0 # 분자

while m:
    _, w, v = heapq.heappop(heap)

    if m <= w: # 용량 m을 다 채울 수 있음
        tempDenomi = m * v
        m -= m
    else: # 용량 m을 다 채울 수 없음
        tempDenomi = w * v
        m -= w

    # 분자
    denomi = (denomi * w) + (tempDenomi * nume)
    
    # 분모
    nume *= w


    # 분모, 분자의 최대공약수 구하기
    gcdValue = getGCD(nume, denomi)

    # 최대공약수로 나누어 기약분수로 만들기
    nume //= gcdValue
    denomi //= gcdValue

print(f'{denomi}/{nume}')

