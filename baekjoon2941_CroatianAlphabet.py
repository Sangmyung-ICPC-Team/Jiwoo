# 크로아티아 알파벳
s = input()
cnt = 0
special_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for s_a in special_alpha:
    s = s.replace(s_a, '*')

print(len(s))