







for _ in range(int(input())):
    
    n, m = map(int, input().split())
    outlets = sorted(map(int, input().split()), reverse=True)

    if n <= 2:
        print(0)
    else:
        currSum = 2
        indx = 0
        while currSum < n and indx < m:
            currSum += outlets[indx] - 1
            indx += 1
        if currSum >= n:
            print(indx)
        else:
            print(-1)