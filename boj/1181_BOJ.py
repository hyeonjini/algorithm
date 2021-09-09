n = int(input())
words = []
for _ in range(n):
    words.append(input())

words = list(set(words)) # map 으로 중복 제거
words = sorted(words, key=lambda x: x) # 단어 기준으로 정렬
words = sorted(words, key=lambda x: len(x)) # 길이 순서로 정렬

for word in words:
    print(word)