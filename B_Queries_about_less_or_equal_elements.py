





n, m = map(int, input().split())

arr1 = sorted(map(int, input().split()))
arr2 = list(map(int, input().split()))

res = []

for each in arr2:
    low, heigh = 0, n - 1
    maxCount = 0
    while low <= heigh:
        mid = low + (heigh - low) // 2
        if each >= arr1[mid]:
            maxCount = max(maxCount, mid + 1)
            low = mid + 1
        else:
            heigh = mid - 1
    res.append(maxCount)

print(*res)