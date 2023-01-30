n = int(input())

def checkColors(row1, row2, colLen):
    i = 0
    for i in range(colLen):
        if row1[i] == 'R'and row2[i] != 'R':
            return 'NO'
        if row2[i] == 'R' and row1[i] != 'R':
            return 'NO'
    return 'YES'

for _ in range(n):
    colLen = int(input())
    row1 = input()
    row2 = input()

    print(checkColors(row1, row2, colLen))

