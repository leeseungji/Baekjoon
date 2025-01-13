import sys

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)

nums.sort(reverse=True)

for num in nums:
    sys.stdout.write(str(num)+'\n')