# 로또 - 백트래킹, 재귀
from sys import stdin

def getLottoNumber(curr_idx, candi_number, length):
    if length == 6:
        print(*selected)
    else:
        for i in range(curr_idx, candi_number):
            selected.append(candi_list[i])
            getLottoNumber(i+1, candi_number, length+1)
            selected.pop()

selected = []
test_case = []
while True:
    test_case.append(list(map(int, stdin.readline().split())))
    if test_case[-1][0] == 0:
        break

for candi_list in test_case:
    n = candi_list[0]
    candi_list = candi_list[1:]
    getLottoNumber(0, n, 0)
    print()