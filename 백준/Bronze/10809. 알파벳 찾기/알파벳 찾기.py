s = input()
words = [-1] * 26

for i in range(len(s)):
    index = ord(s[i]) - ord('a')
    if words[index] == -1:
        words[index] = i

print(' '.join(map(str, words)))