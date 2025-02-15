n, k = map(int, input().split())
heights = list(map(int, input().split()))

differs = []

for i in range(1, n):
    differs.append(heights[i] - heights[i - 1])

differs.sort(reverse = True)

ans = sum(differs[k-1:])

print(ans)