






n, k = map(int, input().split())

resto = []

for _ in range(n):
    resto.append(list(map(int, input().split())))


maxJoy = float('-inf')
for each in resto:
    if each[1] > k:
        maxJoy = max(maxJoy, (each[0] - (each[1] - k)))
    else:
        maxJoy = max(maxJoy, each[0])

print(maxJoy)