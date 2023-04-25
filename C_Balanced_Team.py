n = int(input())
skills = sorted(map(int, input().split()))

maxNum = 0
indx = 0

for i in range(n):

    while indx < n and skills[indx] - skills[i] <= 5:
        indx += 1
    maxNum = max(maxNum, indx - i)

print(maxNum)
