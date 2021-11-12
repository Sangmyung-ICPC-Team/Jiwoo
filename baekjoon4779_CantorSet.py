# 칸토어 집합
while True:
    try:
        n = int(input())

        result = '-'
        before = result

        for i in range(n):
            result = before + ' ' * (3 ** i) + before
            before = result

        print(result)
    except:
        break
