from collections import defaultdict
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest

def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        graph = defaultdict(list)

        for _ in range(m):
            v1, v2 = map(int, input().split())
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        for v in list(graph.keys()):
            x = len(graph[v])
            if x <= 1:
                continue
            y = None 
            for neib in graph[v]:
                if y is None or (y == len(graph[neib]) and y > 1):
                    y = len(graph[neib])
                else:
                    y = -1
                    break
            if y != -1 and y is not None:
                print(x, y - 1)
                break


if __name__ == '__main__':
    main()