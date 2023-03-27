




from math import ceil
n, d = map(int, input().split())

powers = sorted(map(int, input().split()))


right = n - 1
res = 0

while n > 0:
    div = ceil(d/powers[right])
    while powers[right] * div <= d:
        div += 1
    # if division is greater than the element we have
    if div > n:
        break
    res += 1
    right -= 1
    n -= div 

print(res)
