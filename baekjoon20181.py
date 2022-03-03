from sys import stdin

n, k = map(int, stdin.readline().split())
food = [0]
food.extend([*map(int, stdin.readline().split())])

dp = [0] * (n+1)
satis = food[1] # 만족도. 초기 만족도 == 첫번째 먹이

s, e = 1, 1
while True:

    dp[e] = max(dp[e], dp[e-1]) # k = 6일 때, 5 4 4 와 같은 경우임

    #    5 + 4 = 9 >= 6 따라서 dp[2]에서 탈피 에너지 3을 얻음
    #    4 + 4 = 8 >= 6 따라서 2~3을 먹어서 얻을 수 있는 탈피 에너지 2
    #    하지만 1~2를 먹는 것이 최대 탈피 에너지를 얻는 방법임
    #    따라서 dp[2] 값을 그대로 가져오는 것이 해를 구하는 길!

    if satis >= k:
        dp[e] = max(dp[e], dp[s-1] + (satis-k)) # 현재 구간의 먹이를 먹기 전까지의 최대 탈피 에너지 + 새로 얻은 탈피 에너지 vs 현재 위치에서의 최대 탈피 에너지

        if s < e:
            satis -= food[s]
        elif s == e:
            e += 1

            if e > n:
                break

            satis = food[e]

        s += 1

    else:
        e += 1

        if e > n:
            break

        satis += food[e]

print(dp[-1])
