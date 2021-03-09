# 가로수
from math import gcd
n = int(input())
tree = [int(input()) for _ in range(n)]

''' 유클리드 호제법(euclidean algorithm)
1. 최대공약수를 구하는 함수를 gcd(x, y)라고 가정
2. x % y == 0 이라면 gcd(x, y) == y가 성립
3. x % y != 0 이라면 gcd(x, y) == gcd(y, x%y)가 성립
4. 2번이 될 때까지 2~3번을 반복
'''

# gcd = lambda a, b: gcd(a, a % b) if a % b else b
g = tree[1] - tree[0] # 인접한 가로수 사이의 간격

for i in range(2, n):
    g = gcd(g, tree[i] - tree[i - 1])

result = (tree[n-1]-tree[0]) // g - n + 1
print(result)