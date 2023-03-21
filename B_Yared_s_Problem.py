



def compute(nums, n): 
    left, right = 0, 1
    while right < n:
      if abs(nums[right] - nums[left]) > 1:
         return 'NO'
      left += 1
      right += 1
    return 'YES'
           
for _ in range(int(input())):

    n = int(input())
    nums = sorted(map(int, input().split()))
    if n == 1:
        print('YES')
    else:
        print(compute(nums, n))




