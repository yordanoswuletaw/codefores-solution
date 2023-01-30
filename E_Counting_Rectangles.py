for _ in range(int(input())):
    n, q = map(int, input().split())

    rectangles, queries = [], []
    for _ in range(n):
        rectangles.append(tuple(map(int, input().split())))
    rectangles.sort()
    for _ in range(q):
        queries.append(tuple(map(int, input().split())))
    
    for query in queries:
        totalArea = 0
        for rec in rectangles:
            if query[0] < rec[0] < query[2] and query[1] < rec[1] < query[3]:
                totalArea += rec[0] * rec[1]
        print(totalArea)
