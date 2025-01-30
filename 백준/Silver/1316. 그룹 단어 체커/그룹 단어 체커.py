n = int(input())
words = []

for _ in range(n):
    word = input().strip()
    words.append(word)

#알파벳 수 구하기
count = 0
for word in words:
    a = set() #빈 집합
    pre_char = ''
    group = True
    
    for char in word:
        if char != pre_char:
            if char in a:
                group = False
                break
                
            a.add(char)
            pre_char = char #변경
    
    if group:
        count += 1
        
print(count)
        