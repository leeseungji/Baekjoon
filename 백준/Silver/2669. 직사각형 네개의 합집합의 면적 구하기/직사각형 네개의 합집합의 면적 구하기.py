nums = list([0] * 100 for _ in range(100))

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            nums[i][j] = 1
ans = 0
for rows in nums:
    for row in rows:
        ans += row
print(ans)