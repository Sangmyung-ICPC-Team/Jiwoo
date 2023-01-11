# 쇠막대기
target = input()
stack = list()
cnt = 0

for i in range(len(target)):
    if target[i] == '(': stack.append(target[i])
    else: # ')' 인 경우
        stack.pop()
        if target[i-1] == '(': # 레이저인 경우
            cnt += len(stack)
        else: # 막대기의 끝인 경우
            cnt += 1
print(cnt)