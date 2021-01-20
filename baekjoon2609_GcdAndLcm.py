# 최대공배수와 최소공약수
n, m = map(int, input().split())
g = 1

for i in range(min(n, m), 0, -1):
    if not n % i and not m % i:
        g = i
        break

print(g)
print(n*m//g)