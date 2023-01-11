# 연속합
from sys import stdin

def get_max_continuous_sum():

    max_sum = seq[0]

    for i in range(1, n):
        if seq[i-1] > 0 and seq[i-1] + seq[i] > 0:
            seq[i] = seq[i] + seq[i-1]

        max_sum = max(max_sum, seq[i])

    return max_sum

n = int(input())
seq = list(map(int, stdin.readline().split()))

print(get_max_continuous_sum())