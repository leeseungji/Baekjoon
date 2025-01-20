import math

a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

c1 = a1 * b2 + a2 * b1
c2 = a2 * b2

#최대공약수 구하기 (기약분수)
gcd = math.gcd(c1, c2)

c1 = c1 // gcd
c2 = c2 // gcd

print(c1, c2)

