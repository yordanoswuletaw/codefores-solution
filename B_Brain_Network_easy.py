from collections import defaultdict, deque

import sys, threading

input = lambda: sys.stdin.readline().strip()


def main():
    n, m = map(int, input().split())

    graph = defaultdict(list)

    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2) 
        graph[v2].append(v1) 

    visited = set()
    cycle = set()
    ans = 'yes'

    def dfs(prev, v):
        nonlocal ans
        if v in visited:
            return 
        
        visited.add(v)
        cycle.add(v)
        for neib in graph[v]:
            if neib in cycle and neib != prev:
                ans = 'no'
                return 
            dfs(v, neib)
        cycle.remove(v)
    dfs(None, 1)
    if len(visited) == n:
        print(ans)
    else:
        print('no')

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
