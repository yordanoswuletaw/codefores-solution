def main():
    for _ in range(int(input())):
        n = int(input())
        nums = sorted(map(int, input().split()))
        
        currSum = 0
        ans = 'YES'
        for i in range(n):
            if (i == 0 and nums[i] != 1) or ( i > 0 and nums[i] > currSum):
                ans = 'NO'
                break
            currSum += nums[i]
        
        print(ans)
if __name__ == '__main__':
    main()