def main():
    n = int(input())
    nums = list(map(int, input().split()))
    rules = input()

    ans = 'YES'
    currMax = 0
    for i in range(n - 1):
        currMax = max(currMax, nums[i])
        if currMax > i + 1 and rules[i] == '0':
            ans = 'NO'
            break

    print(ans)

if __name__ == '__main__':
    main()
