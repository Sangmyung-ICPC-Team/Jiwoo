# 수학은 체육과목 입니다3
num = input()

for init_digit in range(1, 4):
    digit = init_digit
    i = 0
    flag = False
    while True:
        prev_num = int(num[i:i+digit])
        i += digit

        if prev_num == 9 or prev_num ==  99:
            digit += 1

        if i >= len(num):
            print(prev_num, prev_num)
            flag = True
            break
        curr_num = int(num[i:i+digit])

        if prev_num + 1 != curr_num:
            break
        elif prev_num + 1 == curr_num and i+digit == len(num):
            print(int(num[0:init_digit]), curr_num)
            flag = True
            break
    if flag:
        break
