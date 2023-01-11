# 링
from sys import stdin

n = int(input())
radius = list(map(int, stdin.readline().split()))

first_radius = radius[0]

for i in range(1, n):
    gcd = min(first_radius, radius[i])
    while gcd > 1:
        if (first_radius % gcd == 0) and (radius[i] % gcd == 0):
            break
        gcd -= 1
    print(f'{int(first_radius/gcd)}/{int(radius[i]/gcd)}')

