a, b = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

ab = sorted(set_a.difference(set_b))
ba = sorted(set_b.difference(set_a))

print(len(ab)+len(ba))