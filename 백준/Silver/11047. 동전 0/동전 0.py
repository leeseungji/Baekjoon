n, k = map(int, input().split())

count = 0

coins = []

for _ in range(n):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse = True)    

for coin in coins:
    count += k // coin
    k %= coin

print(count)
