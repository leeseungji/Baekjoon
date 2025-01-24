n = int(input())

count = 0

while True:
    if n % 5 == 0:
        count += n // 5
        print(count)
        break
     
    elif n > 0:
        n -= 3 # 5의 배수가 아니면 3kg 부터 빼고 다시 if 문 돌리기
        count += 1
    
    else:
        print(-1)
        break