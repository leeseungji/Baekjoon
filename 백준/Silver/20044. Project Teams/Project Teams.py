n = int(input())
nums = list(map(int, input().split()))

nums.sort()

print(min(nums[i] + nums[2 * n - 1 - i] for i in range(n)))