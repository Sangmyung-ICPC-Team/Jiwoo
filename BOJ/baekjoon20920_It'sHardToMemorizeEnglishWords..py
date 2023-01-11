# 영단어 암기는 괴로워
from sys import stdin
from collections import defaultdict

n, m = map(int, input().split())
word_dict = defaultdict(int)

for _ in range(n):
    word = stdin.readline().rstrip()

    if len(word) >= m:
        word_dict[word] += 1

word_list = [(word, freq) for word, freq in word_dict.items()]

# 빈도, 길이, 사전순 정렬
word_list = sorted(word_list, key = lambda x: (-x[1], -len(x[0]), x[0]))

for word, freq in word_list:
    print(word)
