


n = int(input())
cards = list(map(int, input().split()))
res = [0, 0]
i, j = 0, n - 1
count = 0
while i <= j:
    maxNum = cards[i]
    if cards[i] < cards[j]:
        maxNum = cards[j]
        j -= 1
    else:
        i += 1
    res[count%2] += maxNum 
    count += 1

print(*res)