# 그룹 단어 체커
n = int(input())
cnt = 0

for _ in range(n):
    group = dict()
    s = input()

    prev = 0
    flag = True
    for ch in s:
        if ch == prev: continue
        else: prev = ch

        if ch not in group:
            group[ch] = True
        else:
            flag = False
            break

    if flag: cnt += 1

print(cnt)