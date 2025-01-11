n = int(input())
times = list(map(int, input().split()))
times.sort()

total_time = 0
current_time = 0

for time in times:
    current_time += time
    total_time += current_time
 
print(total_time)
