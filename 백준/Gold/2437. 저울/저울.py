n = int(input())
weights = list(map(int, input().split()))

weights.sort()

last = 1

for weight in weights:
    if weight > last:
        break
    
    last += weight

print(last)