a, b = map(int, input().split())

def findGCD(a, b):
    if b == 0:
        return a
    return findGCD(b, a % b)


gcd = a 

for num in range(a + 1, b + 1):
    gcd = findGCD(max(gcd, num), min(gcd, num))

print(gcd)