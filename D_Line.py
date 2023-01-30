n = int(input())

for _ in range(n):
    k = int(input())
    persons = input()
    lineSum = 0
    res = []
    for i, person in enumerate(persons): 
        if person == 'L':
            lineSum += i 
        else:
            lineSum += (k - i - 1)
    ptr1, ptr2 = 0, k - 1
    i = 0
    while i < k and ptr1 <= ptr2:
        if i % 2 == 0:
            if persons[ptr1] == 'L':
                lineSum -= ptr1
                lineSum += (k - ptr1 - 1)   #RRL
                if res:
                    res.append(max(res[-1], lineSum))
                else:
                    res.append(lineSum)
            ptr1 += 1
        else:
            if persons[ptr2] == 'R':
                lineSum -= (k - ptr2 - 1)
                lineSum += ptr2 
                if res:
                    res.append(max(res[-1], lineSum))
                else:
                    res.append(lineSum)
            ptr2 -= 1
        i += 1
    for _ in range(len(res), k):
        if res:
            res.append(res[-1])
        else:
            res.append(lineSum)
    print(' '.join(map(lambda r: str(r), res)))
        


            