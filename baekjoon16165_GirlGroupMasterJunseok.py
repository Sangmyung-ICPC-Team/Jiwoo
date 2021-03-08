# 걸그룹 마스터 준석

n, m = map(int, input().split())
girlGroup = {}
answers = []

for _ in range(n):
    team = input()
    num = int(input())

    girlGroup[team] = sorted([input() for _ in range(num)])

for _ in range(m):
    ques = input()
    quesType = input()

    if quesType == '0':
        answers.extend(list(girlGroup[ques]))
    else:
        for team in girlGroup.keys():
            if ques in girlGroup[team]:
                answers.append(team)
                break

for answer in answers:
    print(answer)