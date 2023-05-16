n = int(input())
cards = list(map(int, input().split()))

pt1 = pt2 = 0
left, right = 0, n - 1
turn = 0
while left <= right:
    if cards[left] >= cards[right]:
        if turn % 2:
            pt2 += cards[left]
        else:
            pt1 += cards[left]
        left += 1
    else:
        if turn % 2:
            pt2 += cards[right]
        else:
             pt1 += cards[right] 
        right -= 1
    turn += 1

print(pt1, pt2)
