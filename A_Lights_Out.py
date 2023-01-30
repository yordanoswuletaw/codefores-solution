lights = []
for i in range(3):
    lights.append(list(map(int, input().split())))

def updateState(i, j):
    output[i][j] = int(not output[i][j])

output = [[1 for i in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        if lights[i][j] != 0 and lights[i][j] % 2:
            output[i][j] = int(not output[i][j])
            if i == 0:
                updateState(i+1, j)
                if j == 0:
                    updateState(i, j+1)
                elif j == 1:
                    updateState(i, j-1)
                    updateState(i, j+1)
                else:
                    updateState(i, j-1)
                    
            elif i == 1:
                updateState(i-1, j)
                updateState(i+1, j)
                if j == 0:
                    updateState(i, j+1)
                elif j == 1:
                    updateState(i, j-1)
                    updateState(i, j+1)
                else:
                    updateState(i, j-1)
            else:
                updateState(i-1, j)
                if j == 0:
                    updateState(i, j+1)
                elif j == 1:
                    updateState(i, j-1)
                    updateState(i, j+1)
                else:
                    updateState(i, j-1)

for i in range(3):
    print(''.join([str(j) for j in output[i]]))
                


            