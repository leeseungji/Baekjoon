n, m = map(int, input().split())

first = list(map(int, input().split()))
second = list(map(int, input().split()))

a = first+second
a.sort()
print(' '.join(map(str,a)))