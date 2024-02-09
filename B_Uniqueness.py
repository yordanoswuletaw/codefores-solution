from collections import Counter, defaultdict
def main():
    n = int(input())
    nums = list(map(int, input().split()))

    ans = n - 1
    for indx in range(n):
        occurance = defaultdict(int)
        validPrfx = True
        for start in range(indx):
            occurance[nums[start]] += 1
            if occurance[nums[start]] > 1:
                validPrfx = False
                break
        
        if not validPrfx:
            continue
        
        farEnd = n 
        for end in range(n - 1, indx - 1, -1):
            num = nums[end]
            occurance[num] += 1
            if occurance[num] == 1:
                farEnd = end 
            else:
                break 
        
        ans = min(ans , farEnd - indx)
        
    print(ans)
    
if __name__ == '__main__':
    main()