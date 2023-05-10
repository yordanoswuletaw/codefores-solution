def main():
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))
       
        while True:
            diff = [0, 0]
            for i in range(n - 1):
                for j in range(i + 1, n):
                    if diff[1] < nums[i] & nums[j]:
                        diff[0] = i 
                        diff[1] = nums[i] & nums[j] 
            
            if diff[1] == 0:
                break 
            nums[diff[0]] = nums[diff[0]] - diff[1]

        print(sum(nums))


if __name__ == '__main__':
    main()

