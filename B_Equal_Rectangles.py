def checkRectangles(sides, n):
    area = None 
    left, right = 1, 4 * n - 2
    while left < right:
        currArea = sides[left] * sides[right]
        if area is None:
            area = currArea
        if sides[left - 1] != sides[left] or sides[right] != sides[right + 1]:
            return 'NO'
        if area != currArea:
            return 'NO'
        left += 2
        right -= 2
        
    return 'YES' 
    

for _ in range(int(input())):
    n = int(input())
    sides = sorted(map(int, input().split()))
    print(checkRectangles(sides, n))

