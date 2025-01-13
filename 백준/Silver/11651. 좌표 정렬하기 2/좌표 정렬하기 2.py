n = int(input())

nums = []

for i in range(n):
    num = input().split()
    nums.append((int(num[0]), int(num[1])))

nums.sort(key = lambda x: (x[1], x[0]))

for num in nums:
    print(num[0], num[1])