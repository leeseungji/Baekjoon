import sys
from collections import Counter

data = sys.stdin.read().strip().split()
n = int(data[0]) 
nums = list(map(int, data[1:])) 

nums.sort()

print(round(sum(nums) / n)) #1
print(nums[n//2]) #2

most_common = Counter(nums).most_common() #빈도수 내림차순
max_common = most_common[0][1] #가장 높은빈도수 

modes = []
for num, cnt in most_common:
    if cnt == max_common:
        modes.append(num)

if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

print(max(nums) - min(nums)) #4