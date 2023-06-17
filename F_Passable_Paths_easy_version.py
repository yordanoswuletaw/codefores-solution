from collections import defaultdict
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest

def main():
    n = int(input())
    graph = defaultdict(set)

    for _ in range(n - 1):
        v1, v2 = map(int, input().split())
        graph[v1].add(v2) 
        graph[v2].add(v1) 
    
    
    q = int(input())
    for _ in range(q):
        m = int(input())
        queries = list(map(int, input().split()))
        v = queries[0]
        ans = 'YES'
        for i in range(1, m):
            if queries[i] not in graph[v]:
                ans = 'NO'
                break
            v = queries[i]

        print(ans)
        
if __name__ == '__main__':
    main()
