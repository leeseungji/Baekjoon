n = input()

if '0' not in n:
    print(-1)
    exit()

if sum(map(int, n)) % 3 != 0:
    print(-1)
    exit()

sorted_n = sorted(n, reverse = True)
print(''.join(sorted_n))