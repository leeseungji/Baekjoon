n = int(input())
words = set() #중복제거

for i in range(n):
    words.add(input().strip()) #집합-> add

sorted_words = sorted(words, key = lambda x: (len(x), x))

for word in sorted_words:
    print(word)