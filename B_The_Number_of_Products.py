def main():
    n = int(input())
    nums = list(map(int, input().split()))
    evenBefore = 0
    oddBefore = 0
    ntvs = 0
    ptvSegments = 0
    for i in range(n):
        if ntvs % 2 == 0:
            evenBefore += 1
        else:
            oddBefore += 1
        if nums[i] < 0:
            ntvs += 1
        if ntvs % 2 == 0:
            ptvSegments += evenBefore
        else:
            ptvSegments += oddBefore
    
    totalSegments = n * (n + 1) // 2
    print(totalSegments - ptvSegments, ptvSegments)

if __name__ == '__main__':
    main()