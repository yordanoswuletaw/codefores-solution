from collections import defaultdict, deque
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
        else:
            return True


def main():
    for _ in range(int(input())): 
        n, m = map(int, input().split())
        unionFind = UnionFind(n)
        edges = []
        graph = defaultdict(list)
        for _ in range(m):
            u, v, w = map(int, input().split())
            edges.append((w, u - 1, v - 1))
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        
        edges.sort(reverse=True)
        min_edge = None 
        for w, u, v in edges:
            if unionFind.union(u, v):
                min_edge = (u, v, w)

        visited = {min_edge[1]: -1}
        target = min_edge[0]
        queue = deque([(min_edge[0], min_edge[1])])
        while queue:
            gparent, parent = queue.popleft()
            if parent == target:
                break
            for child in graph[parent]:
                if child != gparent and child not in visited:
                    visited[child] = parent
                    queue.append((parent, child))
        
        nodes = []
        while target != -1:
            nodes.append(target)
            target = visited[target]   
        print(min_edge[2], len(nodes))
        print(*[node + 1 for node in nodes])

if __name__ == '__main__':
    main()



# from collections import defaultdict
# import sys, threading

# input = lambda: sys.stdin.readline().strip()

# class UnionFind:
#     def __init__(self, size):
#         self.root = [i for i in range(size)]
#         self.size = [1] * size

#     def find(self, x):
#         while x != self.root[x]:
#             self.root[x] = self.root[self.root[x]]
#             x = self.root[x]
#         return x
    
#     def union(self, x, y):
#         rootX = self.find(x)
#         rootY = self.find(y)
#         if rootX != rootY:
#             if self.size[rootX] > self.size[rootY]:
#                 self.root[rootY] = rootX
#                 self.size[rootX] += self.size[rootY]
#             else:
#                 self.root[rootX] = rootY
#                 self.size[rootY] += self.size[rootX]
#         else:
#             return True


# def main():
#     for _ in range(int(input())): 
#         n, m = map(int, input().split())
#         unionFind = UnionFind(n)
#         edges = []
#         for _ in range(m):
#             u, v, w = map(int, input().split())
#             edges.append((w, u - 1, v - 1))
        
#         def dfs(src, parent, node):
#             if src == node:
#                 return nodes
#             if colors[node] == 1:
#                 return
#             if colors[node] == 2:
#                 return 

#             nodes.append(node)
#             colors[node] = 1    
#             for v in graph[node]:
#                 if parent == v:
#                     continue
#                 if dfs(src, node, v):
#                     return nodes
#             colors[node] = 2       
#             nodes.pop()
        
#         edges.sort(reverse=True)
#         graph = defaultdict(list)
#         min_edge = None 
#         for w, u, v in edges:
#             if unionFind.union(u, v):
#                 min_edge = (u, v, w)
#             graph[u].append(v)
#             graph[v].append(u)

#         nodes = [min_edge[0]]
#         colors = [0] * n 
#         colors[min_edge[0]] = 1
#         dfs(min_edge[0], min_edge[0], min_edge[1])
#         print(min_edge[2], len(nodes))
#         print(*[node + 1 for node in nodes])

# if __name__ == '__main__':
    
#     sys.setrecursionlimit(1 << 30)
#     threading.stack_size(1 << 27)

#     main_thread = threading.Thread(target=main)
#     main_thread.start()
#     main_thread.join()
 
 
 
 
