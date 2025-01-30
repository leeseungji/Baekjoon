n = int(input())
sentences = []

for _ in range(n):
    sentence = input().strip()
    sentences.append(sentence)

for sentence in sentences:
    words = sentence.split()
    reversed_words = []
    
    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)

    print(' '.join(reversed_words)) #list 안 숫자 없으므로 map str 사용X