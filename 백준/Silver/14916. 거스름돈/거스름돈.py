#그리디 알고리즘
n = int(input())
count = 0

while n > 0:
    if n % 5 == 0:
        count += n // 5
        break
    
    elif n >= 2: #2원 이상
        n -= 2
        count += 1
    
    else:
        count = -1
        break

print(count)