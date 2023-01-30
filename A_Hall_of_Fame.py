testCases = int(input())

for _ in range(testCases):
    n = int(input())
    trophies = input()
    i, j = 0, n - 1
    result = - 1
    while i < j:
        if trophies[i] == 'R' and trophies[j] != 'L':
           break
        if trophies[i] != 'R':
            i += 1
        if trophies[j] != 'L':
            j -= 1
        i += 1
        j -= 1
    
    if i == 0 and j == n - 1:
        print(0)
    elif i < j:
        print(max())    