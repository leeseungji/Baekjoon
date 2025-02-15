n = input()

words = []

for i in range(len(n)):
    words.append(n[i:])

words.sort()

print('\n'.join(words))
