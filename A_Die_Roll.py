import math

y, w = map(int, input().split())
m = max(y, w)
n = 7 - m
d = 6
g = math.gcd(n, d)
print(f"{n // g}/{d // g}")