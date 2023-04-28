def main():
    n, q = map(int,input().split())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    prfxSum = [0] * (n + 1)

    for _ in range(q):
        start, end = map(int, input().split())
        prfxSum[start - 1] += 1
        prfxSum[end] -= 1

    for i in range(1, len(prfxSum)):
        prfxSum[i] += prfxSum[i - 1]

    prfxSum.sort(reverse=True)   

    maxSum = 0
    for i in range(n):      
        if prfxSum[i] == 0:
            break
        maxSum += prfxSum[i] * nums[i]
    
    print(maxSum)

if __name__ == '__main__':
    main()


