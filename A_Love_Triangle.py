def main():
    n = int(input())
    nums = list(map(int, input().split())) 

    for i in range(n):
        num = nums[i] - 1
        if i == nums[nums[num] - 1] - 1:
            print('YES')
            exit()
    print('NO')

if __name__ == '__main__':
    main()