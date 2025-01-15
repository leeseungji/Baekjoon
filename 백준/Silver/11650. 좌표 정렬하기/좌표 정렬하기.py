n = int(input())
nums = []

for i in range(n):
    x, y = map(int, input().split())
    nums.append((x, y)) # 튜플

nums.sort()

for x, y in nums:
    print(x, y)