from collections import defaultdict
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest
import sys, threading

input = lambda: sys.stdin.readline().strip()


def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    edges = defaultdict(int)

    def dfs(v, visited):
        if v in visited:
            return
        visited.add(v)
        if v in graph:
            edges[len(graph[v])] += 1
        for neib in graph[v]:
            dfs(neib, visited)

    visited = set()
    for v in range(1, n + 1):
        if v not in visited:
            dfs(v, visited)
    
    if len(edges) == 1 and edges[2] == n:
        print('ring topology')
    elif len(edges) == 2:
        if edges[1] == 2 and edges[2] == n - 2:
             print('bus topology')
        elif edges[1] == n - 1 and edges[n-1] == 1:
             print('star topology')
        else:
            print('unknown topology')
    else:
        print('unknown topology')
    


if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
 