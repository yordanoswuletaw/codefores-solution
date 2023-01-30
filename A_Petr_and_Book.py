pageNum = int(input())
pages = tuple(map(int, input().split()))

indx = 0
while True:
    pageNum -= pages[indx]
    indx = (indx + 1) % len(pages)
    if pageNum <= 0:
        if indx == 0:
            print(len(pages))
        else:
            print(indx)
        break
