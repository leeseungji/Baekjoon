aa = []

for _ in range(10):
    num = int(input())
    a = num % 42
    aa.append(a)

print(len(set(aa)))