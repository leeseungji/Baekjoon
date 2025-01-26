k = int(input())
nums = []

for _ in range(k):
    num = int(input())
    
    if num == 0:
        if nums:
            nums.pop()
    else:
        nums.append(num)
print(sum(nums))