
def main():
    for _ in range(int(input())):
        n = int(input())
        nums = sorted(list(map(int, input().split())))
        odds = 0

        while odds < n - 1:
            odds = 0
            indx = n - 1
            for i in range(n - 1, -1, -1):
                if nums[i] % 2 and nums[i] != 1:
                    indx = i
                    break 
            
            for i in range(n):
                if i == indx:
                    continue
                while nums[i] % 2 == 0:
                    nums[indx] *= 2
                    nums[i] //= 2
                if nums[i] % 2:
                    odds += 1
        
        print(sum(nums))

if __name__ == '__main__':
    main()