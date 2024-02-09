import math

def norm(p):
    if p[0] < 0:
        p[0] *= -1
        p[1] *= -1
    elif p[0] == 0 and p[1] < 0:
        p[1] *= -1
    d = math.gcd(abs(p[0]), abs(p[1]))
    p[0] //= d
    p[1] //= d

m = {}

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
cnt0 = 0

for i in range(n):
    if a[i] == 0:
        if b[i] == 0:
            cnt0 += 1
    else:
        p = [-b[i], a[i]]
        norm(p)
        p = tuple(p)
        if p in m:
            m[p] += 1
        else:
            m[p] = 1
        ans = max(ans, m[p])

print(cnt0 + ans)
