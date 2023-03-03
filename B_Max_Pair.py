

n = int(input())
boys = sorted(map(int, input().split()), reverse=True)
m = int(input())
girls = sorted(map(int, input().split()), reverse=True)

ptr1 = ptr2 = 0
maxNum = 0

while ptr1 < n and ptr2 < m:
    diff = abs(boys[ptr1] - girls[ptr2])
    if 0 <= diff <= 1:
        maxNum += 1
        ptr1 += 1
        ptr2 += 1
    elif boys[ptr1] > girls[ptr2]:
        ptr1 += 1
    else:
        ptr2 += 1
print(maxNum)