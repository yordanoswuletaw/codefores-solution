





num = input()


steps = 0
while len(num) > 1:
    num = str(sum(map(int, num)))
    steps += 1

print(steps)