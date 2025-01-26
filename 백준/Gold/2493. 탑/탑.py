n = int(input())
heights = list(map(int, input().split()))

stack = []
result = [0] * n

for i in range(n): # stack[높이][인덱스]
    while stack and stack[-1][0] < heights[i]:
        stack.pop()
    
    if stack:
        result[i] = stack[-1][1] + 1
        
    
    stack.append((heights[i], i)) #두개 이상의 값 -> 튜플
    
    
print(' '.join(map(str, result)))