from collections import defaultdict
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest

def main():
    n = int(input())
    sets = list((w, i + 1) for i, w in enumerate(map(int, input().split())))
    heapify(sets)
    psngrs = list(input())
    introvert = []
    res = []

    for p in psngrs:
        if p == '0':
            w, i = heappop(sets)
            res.append(i)
            heappush(introvert, (-w, i)) 
        else:
            w, i = heappop(introvert) 
            res.append(i)
    
    print(*res)

    
if __name__ == '__main__':
    main()