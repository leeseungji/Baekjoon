from collections import Counter
n, c = map(int, input().split())
nums = list(map(int, input().split()))

a = Counter(nums)

order = {}
for index, num in enumerate(nums):
    if num not in order:
        order[num] = index
        
sorted_nums = sorted(nums, key = lambda x: (-a[x], order[x]))

print(*sorted_nums)