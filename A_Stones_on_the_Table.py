n = int(input())
stones = input()

minNum = 0
for i in range(1, n):
    if stones[i-1] == stones[i]:
        minNum += 1
print(minNum)