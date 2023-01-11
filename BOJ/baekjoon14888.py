# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

def backtrack(k, total, p, s, m, d):
    global max_v, min_v

    if k >= n:
        max_v = max(max_v, total)
        min_v = min(min_v, total)
    else:
        if p:
            backtrack(k + 1, total + nums[k], p - 1, s, m, d)
        if s:
            backtrack(k + 1, total - nums[k], p, s - 1, m, d)
        if m:
            backtrack(k + 1, total * nums[k], p, s, m - 1, d)
        if d:
            if total // nums[k] < 0:
                backtrack(k + 1, -(-total // nums[k]), p, s, m, d - 1)
            else:
                backtrack(k + 1, total // nums[k], p, s, m, d - 1)


n = int(input())
nums = [*map(int, input().split())]
num_op = [*map(int, input().split())]

max_v = -1e9
min_v = 1e9

backtrack(1, nums[0], num_op[0], num_op[1], num_op[2], num_op[3])

print(max_v)
print(min_v)
