from sys import stdin

input = stdin.readline

n, q = map(int, input().split())

domino = [0] * (n+1)
xorResult = [0] + [*map(int, input().split())]


for i in range(2, n+1):
    
    domino[i] = domino[i-1] ^ xorResult[i-1]
    
for _ in range(q):
    
    command = [*map(int, input().split())]
    
    if len(command) == 3: # 0 x yield
        _, x, y = map(int, command)
        
        print(domino[x] ^ domino[y])
        
    else:
        _, x, y, d = map(int, command)
        
        print(domino[x] ^ domino[y] ^ d)
    