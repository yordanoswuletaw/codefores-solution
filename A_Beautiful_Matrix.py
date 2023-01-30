row = col = 0
for i in range(5):
    currRow = tuple(map(int, input().split()))
    for j in range(len(currRow)):
        if currRow[j] == 1:
            row = i 
            col = j 

print(abs(2-row) + abs(2-col))
