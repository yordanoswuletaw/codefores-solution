def findPairs(nums, n, maxVal):
    left, right = 0, n - 1
    pairs = 0

    while left < right:
        if nums[left] + nums[right] <= maxVal:
            pairs += right - left
            left += 1
        else:
            right -= 1
    
    return pairs

def main():
    for _ in range(int(input())):
        n, l, r = map(int, input().split())
        nums = sorted(map(int, input().split()))

        maxPairs = findPairs(nums, n, r)
        minPairs = findPairs(nums, n, l - 1)
        
        print(maxPairs - minPairs)

if __name__ == '__main__':
    main()

