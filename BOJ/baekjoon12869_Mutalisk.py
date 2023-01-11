# 뮤탈리스크

def attackSCV(p1, p2, p3):
    if p1 <= 0 and p2 <= 0 and p3 <= 0:
        return 0

    if p1 < 0: p1 = 0
    if p2 < 0: p2 = 0
    if p3 < 0: p3 = 0

    if damage_cnt[p1][p2][p3]:
        return damage_cnt[p1][p2][p3]
    else:
        damage_cnt[p1][p2][p3] = min(attackSCV(p1 - 9, p2 - 3, p3 - 1),
                                     attackSCV(p1 - 9, p2 - 1, p3 - 3),
                                     attackSCV(p1 - 3, p2 - 9, p3 - 1),
                                     attackSCV(p1 - 3, p2 - 1, p3 - 9),
                                     attackSCV(p1 - 1, p2 - 9, p3 - 3),
                                     attackSCV(p1 - 1, p2 - 3, p3 - 9)) + 1

        return damage_cnt[p1][p2][p3]

scv_powers = [0, 0, 0]

n = int(input())

if n == 1: scv_powers[0] = int(input())
elif n == 2: scv_powers[0], scv_powers[1] = map(int, input().split())
else: scv_powers = [*map(int, input().split())]

damage_cnt = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]

print(attackSCV(scv_powers[0], scv_powers[1], scv_powers[2]))
