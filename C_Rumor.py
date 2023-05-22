import sys, threading
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())
    golds = {i + 1: gold for i, gold in enumerate(map(int, input().split()))}
    graph = defaultdict(list)
    visited = set()

    for _ in range(m):
        f1, f2 = map(int, input().split())
        graph[f1].append(f2)
        graph[f2].append(f1)
    
    def dfs(v, visited, minGold):
        visited.add(v)
        minGold = min(minGold, golds[v])
        for neib in graph[v]:
            if neib not in visited:
                minGold = min(minGold, dfs(neib, visited, minGold))
        return minGold
    
    minGolds = 0

    for v in range(1, n + 1):
        if v not in visited: 
            minGolds += dfs(v, visited, float('inf'))

    for node in range(1, n + 1):
        if node not in visited:
            minGolds += golds[node]
    
    print(minGolds)

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
 
