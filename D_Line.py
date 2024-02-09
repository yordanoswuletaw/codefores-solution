def main():
    for _ in range(int(input())):
        n = int(input())
        lines = input()
        values = []
        totCount = 0
        # getting the total counts of each person in current line
        # and getting the maximized count of each persons by swapping the persons view direction
        for i, line in enumerate(lines):
            if line == 'L':
                totCount += i
                values.append(max(i, n - i - 1) - i)
            else:
                totCount += (n - i - 1)
                values.append(max(i, n - i - 1) - (n - i - 1))
        
        # sort values in decreasing order to maximize the counts
        values.sort(reverse=True)
        for i in range(len(values)):
            totCount += values[i]
            values[i] = totCount
        
        print(*values) 

if __name__ == '__main__':
    main()
# n = int(input())

# for _ in range(n):
#     k = int(input())
#     persons = input()
#     lineSum = 0
#     res = []
#     for i, person in enumerate(persons): 
#         if person == 'L':
#             lineSum += i 
#         else:
#             lineSum += (k - i - 1)
#     ptr1, ptr2 = 0, k - 1
#     i = 0
#     while i < k and ptr1 <= ptr2:
#         if i % 2 == 0:
#             if persons[ptr1] == 'L':
#                 lineSum -= ptr1
#                 lineSum += (k - ptr1 - 1)   #RRL
#                 if res:
#                     res.append(max(res[-1], lineSum))
#                 else:
#                     res.append(lineSum)
#             ptr1 += 1
#         else:
#             if persons[ptr2] == 'R':
#                 lineSum -= (k - ptr2 - 1)
#                 lineSum += ptr2 
#                 if res:
#                     res.append(max(res[-1], lineSum))
#                 else:
#                     res.append(lineSum)
#             ptr2 -= 1
#         i += 1
#     for _ in range(len(res), k):
#         if res:
#             res.append(res[-1])
#         else:
#             res.append(lineSum)
#     print(' '.join(map(lambda r: str(r), res)))
        


            