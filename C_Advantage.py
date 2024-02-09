n = int(input())

for _ in range(n):
    numsLen = int(input())
    nums = list(map(int, input().split()))
    firstMax, secondMax = 0, 0
    output = []

    for num in nums:
        if firstMax < num:
            secondMax = firstMax
            firstMax = num 
        elif secondMax < num:
            secondMax = num

    for num in nums:
        if num == firstMax:
            output.append(str(num - secondMax))
        else:
            output.append(str(num - firstMax))
            
    print(' '.join(output))
    