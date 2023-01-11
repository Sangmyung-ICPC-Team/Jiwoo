# 중복 빼고 정렬하기
from sys import stdin
input = stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))

curr = arr[0]
print(curr, end=' ')

for i in range(1, n):
    if curr != arr[i]:
        curr = arr[i]
        print(curr, end=' ')