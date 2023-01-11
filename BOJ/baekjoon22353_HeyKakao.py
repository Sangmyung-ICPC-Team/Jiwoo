# 헤이카카오
a, d, k = map(int, input().split())
play_time = 0.0
prob_lose = 1.0
curr_round = 0

while True:
    curr_round += 1

    if d >= 100:
        d = 100

    # 이번 판에 이길 확률
    play_time += (a * curr_round) * prob_lose * d / 100

    if d == 100:
        break

    prob_lose *= (100 - d) / 100
    d += d * k / 100

print('%.7f' % play_time)
