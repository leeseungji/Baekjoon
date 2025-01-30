a, b = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

ans = sorted(set_a.difference(set_b))

if ans:
    print(len(ans))
    print(*ans)

else:
    print(0)