# 파도반 수열
def get_padovan_sequence(num):
    if num == 0:
        return 0
    if padovan_seq[num]:
        return padovan_seq[num]
    else:
        padovan_seq[num] = get_padovan_sequence(num-1) + get_padovan_sequence(num-5)
        return padovan_seq[num]

padovan_seq = [0]*101
padovan_seq[1] = padovan_seq[2] = padovan_seq[3] = 1
padovan_seq[4] = padovan_seq[5] = 2

answer = list()
t = int(input())

for _ in range(t):
    n = int(input())

    if n < 6: answer.append(padovan_seq[n])
    else: answer.append(get_padovan_sequence(n))

for a in answer: print(a)