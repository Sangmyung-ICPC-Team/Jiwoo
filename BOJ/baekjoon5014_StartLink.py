from sys import stdin

f, s, g, u, d = map(int, stdin.readline().split())

min_push = [-1 for _ in range(f+1)]
min_push[s] = 0

queue = list()
queue.append(s)

next_floor = [u, -d]

while queue:
    curr_floor = queue.pop(0)

    if curr_floor == g:
        break

    for next in next_floor:
        if (1 <= curr_floor+next <= f) and (min_push[curr_floor+next] == -1):
            min_push[curr_floor+next] = min_push[curr_floor]+1
            queue.append(curr_floor+next)

print(min_push[g]) if min_push[g] != -1 else print("use the stairs")