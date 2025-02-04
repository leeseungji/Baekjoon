n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

c =  list([0] * k for _ in range(n)) #행렬 초기화

for i in range(n):
    for j in range(k):
        for q in range(m):
            c[i][j] += a[i][q] * b[q][j]

for row in c:
    print(*row)