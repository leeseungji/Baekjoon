n = int(input())
results = []

for _ in range(n):
    nums = list(map(int, input().split()))
    nums.sort(reverse = True)
    results.append(nums[2])

for result in results:
    print(result)
