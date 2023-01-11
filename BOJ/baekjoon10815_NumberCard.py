# 숫자 카드
def binary_search(target):
    s = 0
    e = len(numbers) - 1
    while s <= e:
        middle = (s + e) // 2

        if target == numbers[middle]:
            return 1
        elif target < numbers[middle]:
            e = middle - 1
        else:
            s = middle + 1
    return 0

input()
numbers = sorted(list(map(int, input().split())))
input()
targets = list(map(int, input().split()))

for t in targets:
    print(binary_search(t), end=" ")