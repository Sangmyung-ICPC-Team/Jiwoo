# 스택 수열
from sys import stdin
input = stdin.readline

def stack_sequence():
    max_num, stack = 0, [0]
    o_result = []

    for s in sequence:
        while stack[-1] < s:
            if max_num >= n:
                print('NO')
                return
            max_num += 1
            stack.append(max_num)
            o_result.append('+')
        while stack[-1] >= s:
            stack.pop()
            o_result.append('-')

    for o in o_result:
        print(o)

n = int(input())
sequence = []

for _ in range(n):
    sequence.append(int(input()))

stack_sequence()