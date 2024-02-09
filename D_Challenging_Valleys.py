for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    indx = 1
    ans = 'YES'
    leftMin = nums[0]
    while indx <= n - 2:
        if leftMin < nums[indx] > nums[indx + 1]:
            ans = 'NO'
            break
        leftMin = min(leftMin, nums[indx])
        indx += 1
    print(ans)


    #i, j = 0, numsLen - 1

    # while i <= j:
    #     if i < j and nums[i] >= nums[i+1]:
    #         i += 1
    #     if j > i and nums[j] >= nums[j-1]:
    #         j -= 1
    #     if i < j and nums[i] < nums[i + 1] and j > i and nums[j] < nums[j-1]:
    #         print('NO')
    #         break
    #     if i == j:
    #         print('YES')
    #         break