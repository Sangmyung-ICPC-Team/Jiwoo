import sys
input = sys.stdin.readline

city_num = int(input())
dis = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_cost = prices[0]
total_cost = 0
for i in range(city_num-1):
    if prices[i] < min_cost:
        min_cost = prices[i]

    total_cost += min_cost * dis[i]

print(total_cost)