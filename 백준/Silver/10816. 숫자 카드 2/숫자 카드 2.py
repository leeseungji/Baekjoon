from collections import Counter
import sys

data = list(map(int, sys.stdin.read().split()))

n = data[0]
nums1 = data[1:n+1]
m = data[n+1]
nums2 = data[n+2:n+2+m]

counter_nums1 = Counter(nums1)

result = []
for num in nums2:
    result.append(counter_nums1[num])

print(' '.join(map(str, result)))