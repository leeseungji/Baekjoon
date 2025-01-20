a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

# 조건 확인
if (a[0] == b[0] and a[1] == b[1] and a[2] == b[2]) and (a[0]*b[0] + a[1]*b[1] == a[2] *b[2]):
    print('YES')
    
else:
    print('NO')
