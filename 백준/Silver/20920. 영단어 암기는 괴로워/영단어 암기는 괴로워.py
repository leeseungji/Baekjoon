import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
words = []
for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) >= m:
        words.append(word)

words_count = Counter(words)
words = list(words_count.keys()) # 횟수 적은 단어만 중복없이
words.sort(key = lambda x: (-words_count[x], -len(x), x))

sys.stdout.write('\n'.join(words) + '\n')