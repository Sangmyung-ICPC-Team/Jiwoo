# 약수
from sys import stdin

n = int(input())
divisors = list(map(int, stdin.readline().split()))

if n == 1:
    print(divisors[0]**2)
elif n == 2:
    print(divisors[0]*divisors[1])
else:
    min_divisor = min(divisors)
    max_divisor = max(divisors)
    print(min_divisor*max_divisor)