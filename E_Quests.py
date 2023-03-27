





def findMax(n, c, d, quests):

    if c < quests[0]:
        return 'Infinity'
    elif c > quests[0] * d:
        return 'Impossible'
    
    low, heigh = 0, d
    maxK = 0
    while low <= heigh:
        mid = low + (heigh - low) // 2
        mul = d // (mid + 1)
        rem = d % (mid + 1)
        currSum = (sum(quests[:mid+1]) * mul) + sum(quests[:rem])

        if currSum >= c:
            maxK = mid
            low = mid + 1
        else:
            heigh = mid - 1

    return maxK

for _ in range(int(input())):
    n, c, d = map(int, input().split())
    quests = sorted(map(int, input().split()), reverse=True)
    print(findMax(n, c, d, quests))



