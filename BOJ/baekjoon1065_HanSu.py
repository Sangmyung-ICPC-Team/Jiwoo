# 한수
n = int(input())

if n < 100:
    print(n)
else:
    cnt = 0
    while n > 99:
        hundred = n//100
        ten = (n%100)//10
        one = (n%10)
        if hundred-ten == ten-one:
            cnt += 1
        n -= 1
    print(99+cnt)
