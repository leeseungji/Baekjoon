import sys

input = sys.stdin.readline

n = int(input())

triangle = []

for _ in range(n):
    triangle.append(int(input()))

triangle.sort(reverse = True)

for i in range(n - 2):
    if triangle[i] < triangle[i+1] + triangle[i+2]:
        print(triangle[i] + triangle[i+1] + triangle[i+2])
        break
    
    else:
        if i == n - 3:
            print(-1)
    