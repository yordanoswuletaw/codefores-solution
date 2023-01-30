



def check(nums, l):
    sum1, res1 = 0, True
    sum2, res2 = 0, True
    
    for i in range(l):
        sum1 += nums[i] 
        if sum1 >= 0:
            res1 = False 
            break
    for i in range(l-1, -1, -1):
        sum2 += nums[i]
        if sum2 <= 0:
            res2 = False
            break
    if res1:
        print('YES')
        print(' '.join(map(str, nums)))
    elif res2:
        print('YES')
        print(' '.join(map(str, nums[::-1])))
    else:
        print('NO')
n = int(input())
for _ in range(n):
    l = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    check(nums, l)