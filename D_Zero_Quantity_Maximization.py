from collections import defaultdict
from fractions import Fraction
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = defaultdict(int)
d = 0
for i in range(n):
    if a[i] != 0:
        q = Fraction(-b[i], a[i])
        c[q] += 1
    elif b[i] == 0:
        d += 1

if c:
    print(d + int(max(c.values())))
else:
    print(0)