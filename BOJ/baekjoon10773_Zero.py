# 제로
n = int(input())
total_sum = 0
note = list()

for _ in range(n):
    num = int(input())
    if num:
        note.append(num)
        total_sum += note[-1]
    else:
        total_sum -= note.pop()

print(total_sum)