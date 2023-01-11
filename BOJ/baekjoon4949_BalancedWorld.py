# 균형잡힌 세상
from sys import stdin

def isBalanced(s):
    balance = list()

    for ch in s:
        if ch == '(' or ch == '[':
            balance.append(ch)
        elif ch == ')':
            if not balance or balance[-1] != '(':
                return False
            else:
                balance.pop()
        elif ch == ']':
            if not balance or balance[-1] != '[':
                return False
            else:
                balance.pop()

    if balance: return False
    else: return True

while True:
    user_str = stdin.readline().rstrip()
    if user_str == '.':
        break
    print('yes') if isBalanced(user_str) else print('no')
