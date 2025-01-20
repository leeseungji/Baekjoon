import heapq
n = int(input())
nums = []
for _ in range(n):
    num = int(input().strip())
    nums.append(num)
heapq.heapify(nums) #nums리스트를 힙으로 !

counts = 0

while len(nums) > 1:
    first = heapq.heappop(nums)
    second = heapq.heappop(nums)
    
    hap = first + second
    counts += hap
    
    heapq.heappush(nums, hap)
    
print(counts)
    