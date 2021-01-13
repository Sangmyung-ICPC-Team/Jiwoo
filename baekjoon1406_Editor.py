# 에디터
from sys import stdin

left_s = list(stdin.readline().strip())
right_s = []
m = int(input())
i = 0

for line in stdin:
    i += 1

    if line[0] == 'L' and left_s:
        right_s.append(left_s.pop())
    elif line[0] == 'D' and right_s:
        left_s.append(right_s.pop())
    elif line[0] == 'B' and left_s:
        left_s.pop()
    elif line[0] == 'P':
        left_s.append(line[2])

    if i == m:
        break

print(''.join(left_s + list(reversed(right_s))))