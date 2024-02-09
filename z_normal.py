from collections import defaultdict
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest
from sys import stdin
def main():
    inp = stdin.readline()
    # write your solution here

if __name__ == '__main__':
    main()

def main():
    n, m = map(int, input().split())
    src, dest = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    visited = {src: None}
    queue = deque([src])

    while queue:
        node = queue.popleft()
        if node == dest:
            break

        for neib in graph[node]:
            if neib not in visited:
                visited[neib] = node 
                queue.append(neib)
    
    if dest in visited:
        paths = deque()
        node = dest
        while node in visited:
            paths.appendleft(node)
            node = visited[node]
        print(len(paths) - 1)
        print(*paths)
    else:
        print(-1)


if __name__ == '__main__':
    main()





# import sys
# from collections import defaultdict
# def main():
#     n = int(sys.stdin.readline())
#     adjMat = []
#     for _ in range(n):
#         adjMat.append(list(map(int, sys.stdin.readline().split())))
    
#     source  = []
#     sink  = []

#     for i in range(n):
#         isSource = True
#         for j in range(n):
#             if i != j and adjMat[j][i] != 0:
#                 isSource =False 
#                 break
#         if isSource:
#             source.append(i + 1) 
    
#     for i in range(n):
#         isSink = True 
#         for j in range(n):
#             if i != j and adjMat[i][j] != 0:
#                 isSink = False
#                 break
#         if isSink:
#             sink.append(i + 1) 
    
#     print(len(source), *source)
#     print(len(sink), *sink)

# if __name__ == '__main__':
#     main()


import sys
from collections import defaultdict
def main():
    n, m = map(int, sys.stdin.readline().split())
    adjList = defaultdict(list)
    degree = [0] * n 
    for _ in range(m):
        v1, v2 = map(int, sys.stdin.readline().split())
        adjList[v1].append(v2)
        adjList[v2].append(v1)
        degree[v1 - 1] += 1
        degree[v2 - 1] += 1
    
    if len(set(degree)) <= 1:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()


# import sys
# from collections import defaultdict
# def main():
#     n = int(sys.stdin.readline())
#     adjMat = [[0 for _ in range(n)] for _ in range(n)]
#     adjList = []

#     for _ in range(n):
#         adjList.append(list(map(int, sys.stdin.readline().split())))
    
#     for i, each in enumerate(adjList):
#         for j in range(1, len(each)):
#             adjMat[i][each[j] - 1] = 1
    
#     for row in adjMat:
#         print(*row)

    
# if __name__ == '__main__':
#     main()


# import sys
# from collections import defaultdict
# def main():
#     n = int(sys.stdin.readline())
#     graph = []
#     adjList = defaultdict(list)

#     for _ in range(n):
#         row = list(map(int, sys.stdin.readline().split()))
#         graph.append(row)
    
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j]:
#                 adjList[i].append(j + 1)
    
#     for key, value in adjList.items():
#         print(len(value), *value)
    
# if __name__ == '__main__':
#     main()


# import sys
# from collections import defaultdict
# def main():
#     n = int(sys.stdin.readline())
#     graph = []
#     hashSet = defaultdict(int)

#     for _ in range(n):
#         row = list(map(int, sys.stdin.readline().split()))
#         graph.append(row)
    
#     for i in range(n):
#         for j in range(n):
#             if i <= j and graph[i][j]:
#                 hashSet[tuple([i,j])] += 1
#             elif graph[i][j]:
#                 hashSet[tuple([j,i])] += 1
    
#     print(len(hashSet))
    
# if __name__ == '__main__':
#     main()


# import sys
# from collections import defaultdict
# def main():
#     n = int(sys.stdin.readline())
#     k = int(sys.stdin.readline())

#     ans = []
#     graph = defaultdict(list)
#     for i in range(k):
#         input = list(map(int, sys.stdin.readline().split()))
#         if input[0] == 1:
#             graph[input[1]].append(input[2])
#             graph[input[2]].append(input[1]) 
#         else:
#             print(*graph[input[1]])
    
# if __name__ == '__main__':
#     main()

