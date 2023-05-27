from collections import deque

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    rules = list(map(int, input()))
    prfxSum = [0]

    for i in range(len(rules)):
        prfxSum.append(prfxSum[-1] + rules[i])

    ans = 'YES'
    for i in range(n - 1):
        if nums[i] > i + 1 and rules[i] == 0:
            ans = 'NO'
            break
        elif nums[i] > i + 1 and rules[i]:
            if prfxSum[nums[i] - 1] - prfxSum[i - 1] < nums[i] - i - 1:
                ans='NO'
                break
    print(ans)

if __name__ == '__main__':

    main()
