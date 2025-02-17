n = int(input())
length = 0
digit = 1 #자릿수
i = 1

while i <= n:
    last = min(n, i * 10 -1)
    length += (last - i + 1) * digit
    i *= 10
    digit += 1

print(length)