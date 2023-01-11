# 합분해
def sum_decompose(m, r):
    for i in range(2, m + 1):
        memo[i] = i * memo[i - 1]

    return (memo[m] // (memo[r] * memo[m-r])) % 1000000000


n, k = map(int, input().split())
memo = [0 for _ in range(n + k)]
memo[0] = memo[1] = 1

print(sum_decompose(n + k - 1, k - 1))