# 단어 정렬
n = int(input())
word_dic = dict()
word_arr = list()

for _ in range(n):
    word = input()
    if word not in word_dic:
        word_dic[word] = 1
        word_arr.append(word)

word_arr.sort() # 사전식 정렬
word_arr = sorted(word_arr, key=lambda x:len(x))

print(*word_arr, sep='\n')