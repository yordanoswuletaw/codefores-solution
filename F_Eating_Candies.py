def main():
    for _ in range(int(input())):
        n = int(input())
        candies = list(map(int, input().split()))
        left, right = 0, n - 1
        maxCandies = 0
        leftSum = [candies[0]]
        rightSum = [0] * n
        rightSum[-1] = candies[-1]

        for i in range(1, n):
            leftSum.append(leftSum[-1] + candies[i])
        for i in range(n - 2, -1, -1):
            rightSum[i] = rightSum[i + 1] + candies[i]

        while left < right:
            if leftSum[left] > rightSum[right]:
                right -= 1
            elif leftSum[left] < rightSum[right]:
                left += 1
            else:
                maxCandies = max(maxCandies, left + 1 + (n - right))
                left += 1
        
        print(maxCandies)


if __name__ == '__main__':
    main()

