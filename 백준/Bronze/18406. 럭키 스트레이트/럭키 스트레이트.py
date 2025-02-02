n = input().strip()

if len(n) % 2 == 0:
    nums = list(map(int, n))
    
    nums_1 = sum(nums[:len(nums) // 2])
    nums_2 = sum(nums[len(nums) // 2:])
    
    if nums_1 == nums_2:
        print('LUCKY')
    else:
        print('READY')
else:
    print('READY')