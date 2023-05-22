import sys, threading
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    
    # constructing the graph
    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = set()
    cyclicNodes = 0

    # iterate over each components 
    for v in range(1, n + 1):
        if v not in visited:
            # checking for cycle in each component
            stack, cyclic = [v], True 
            while stack:
                top = stack.pop()
                if top not in visited:
                    visited.add(top)
                    # if the vertix has 2 less or more children then this component is not cyclic
                    if len(graph[top]) != 2 and cyclic:
                        cyclic = False 
                        
                    for neib in graph[top]:
                        stack.append(neib)

            if cyclic:
                cyclicNodes += 1
    
    print(cyclicNodes)

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
 
