import sys, threading
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()


def main():
    for _ in range(int(input())):
        n = int(input())
        nodes = list(map(int, input().split()))
        colors = {node + 1: color for node, color in enumerate(input())}

        graph = defaultdict(list)

        for i in range(2, n + 1):
            graph[nodes[i - 2]].append(i)
        
        count = 0
        def dfs(v):
            nonlocal count
            B, W = 0, 0
            if colors[v] == 'B':
                B += 1
            else:
                W += 1
            for edge in graph[v]:
                b, w = dfs(edge)
                B += b 
                W += w 
            if B == W:
                count += 1

            return B, W

        dfs(1) 
        print(count)


if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
 
