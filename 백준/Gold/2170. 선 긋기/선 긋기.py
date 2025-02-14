import sys
input = sys.stdin.readline

n = int(input().strip())
nums = []

for _ in range(n):
    x, y = list(map(int, input().split()))
    nums.append((x, y))

nums.sort() #x기준

total = 0
start, end = nums[0]

for x, y in nums[1:]:
    if x <= end:
        end = max(end, y)
    
    else:
        total += end - start
        start, end = x, y

total += end - start

print(total)