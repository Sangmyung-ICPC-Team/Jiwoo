# 소수 구하기
from sys import stdout

def isDecimal(k):
    if k == 1:
        return False
    else:
        for i in range(2, 1+int(k**0.5)):
            if k % i == 0:
                return False
        return True

m, n = map(int, input().split())

for t in range(m, n+1):
    if isDecimal(t):
        stdout.write(str(t)+'\n')