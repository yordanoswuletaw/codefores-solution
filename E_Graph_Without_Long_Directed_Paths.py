import sys, threading
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    edges = []

    for _ in range(m):
        v1, v2 = map(int, input().split())
        edges.append((v1, v2))
        graph[v1].append(v2) 
        graph[v2].append(v1) 
    
    colors = {}
    colors[1] = 1
    stack = [1]
    canDirected = True 
    while stack:
        top = stack.pop()
        for neib in graph[top]:
            if neib in colors:
                if colors[neib] == colors[top]:
                    canDirected = False
                    break
            else:
                colors[neib] = 1 - colors[top]
                stack.append(neib)

    if canDirected:
        result = []
        print('YES')
        for v1, v2 in edges:
            result.append(str(int(colors[v1] and not colors[v2])))
        print(''.join(result))
    else:
        print('NO')

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
 
