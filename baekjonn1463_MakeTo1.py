# 1로 만들기 - DP(Bottom-up)
INF = 100
def get_min_calc_count(curr_num):

    for i in range(2, n+1):
        if i%3 == 0:
            min_calc[i] = min(min_calc[i], 1+min_calc[i//3])
        if i%2 == 0:
            min_calc[i] = min(min_calc[i], 1+min_calc[i//2])
        min_calc[i] = min(min_calc[i], 1+min_calc[i-1])

    return min_calc[curr_num]

n = int(input())
if n == 1:
    print(0)
else:
    min_calc = [INF for _ in range(n+1)]
    min_calc[1] = 0
    print(get_min_calc_count(n))