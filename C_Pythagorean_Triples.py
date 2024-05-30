n = int(input())
MAX = 10 ** 9


# n as hypotenuse
for a in range(1, int(MAX ** 0.5)):
    b = (n ** 2 - a ** 2) ** 0.5
    if int(b) == 0:
        break
    if b == int(b) and b  < n:
        print(a, int(b))
        exit(0)
# n as cathetus
for a in range(n ** 2, int((10 ** 9))):
    b = (a ** 2 - n ** 2) ** 0.5
    if int(b) == 0:
        break
    if b!= 0 and b == int(b) and b < a:
        print(a, int(b))
        exit(0)

print(-1)