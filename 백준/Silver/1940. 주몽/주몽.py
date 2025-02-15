n = int(input())
m = int(input())

nums = list(map(int, input().split()))

nums.sort()

left, right = 0, n - 1
count = 0

while left < right:
    total = nums[left] + nums[right]

    if total == m:
        count += 1
        left += 1
        right -= 1
    
    elif total < m:
        left += 1
   
    else:
        right -= 1

print(count)