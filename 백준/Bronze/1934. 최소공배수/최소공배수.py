import math

n = int(input())
nums = []

for _ in range(n):
    a, b = map(int, input().split())
    c = math.lcm(a,b)
    print(c)