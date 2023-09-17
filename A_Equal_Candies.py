def main():
    for _ in range(int(input())):
        n = int(input())
        nums = sorted(map(int, input().split()))

        res = 0
        for num in nums:
            res += num - nums[0]

        print(res) 

if __name__ == '__main__':
    main()