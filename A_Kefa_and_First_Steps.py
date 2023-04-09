



n = int(input())
nums = list(map(int, input().split()))

maxSeg = currSeg = 1
i, j = 0, 1

while j < n:
    if nums[j -1] > nums[j]:
        maxSeg = max(maxSeg, currSeg)
        i = j
        currSeg = 0
    currSeg += 1
    j += 1

print(max(currSeg, maxSeg))
