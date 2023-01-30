n = int(input())

for _ in range(n):
    nameLen = int(input())
    name = sorted(input())
    timur = sorted('Timur')
    if name == timur:
        print('YES')
    else:
        print('NO')
