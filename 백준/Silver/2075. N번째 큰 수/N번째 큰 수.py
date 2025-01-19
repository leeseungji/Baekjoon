import heapq

n = int(input())
heap = []

for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums:
        if len(heap) < n : #heap의 길이가 n보다 작으면 nums의 새로운 수 push할 수 있음
            heapq.heappush(heap, num)
        
        else:
            if num > heap[0]: # 남아있는 수가 heap[0] 보다 클 때, heap[0] 수 pop
                heapq.heappushpop(heap, num)
                #nums의 새로운 수 추가하면서 동시에 제일 작은 수 pop하므로 push pop
print(heap[0])
        