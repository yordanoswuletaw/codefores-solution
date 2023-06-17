import sys, threading
from collections import defaultdict
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest

# input = lambda: sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        v1, v2 = map(int, input().split())
        heappush(graph[v1], v2)
        heappush(graph[v2], v1)
    
    heap = [1]
    visited = set()
    heapify(heap)
    res = []
    
    while heap:
        v = heappop(heap)
        if v not in visited:
            visited.add(v)
            res.append(v)
            for neib in graph[v]:
                if neib not in visited:
                    heappush(heap, neib)
    
    print(*res)

if __name__ == '__main__':
    main()
 
