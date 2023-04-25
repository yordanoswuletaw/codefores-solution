for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    stack = [nums[0]]
    for i in range(1, n):
        if nums[i] > 0:
            if stack[-1] > 0:
                stack[-1] = max(stack[-1], nums[i]) 
            else:
                stack.append(nums[i]) 
        else:
            if stack[-1] > 0:
                stack.append(nums[i]) 
            else:
                stack[-1] = max(stack[-1], nums[i])  
                
    print(sum(stack))
