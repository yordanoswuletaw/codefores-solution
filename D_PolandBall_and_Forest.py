from collections import defaultdict
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
    n = int(input())
    seq = list(map(int, input().split()))
    adjList = defaultdict(list)

    for i in range(1, n + 1):
        adjList[i].append(seq[i - 1])
        adjList[seq[i - 1]].append(i)
    
    counts = 0
    visited = set()

    def dfs(vertix):
        if vertix in visited:
            return
        visited.add(vertix)
        for nighbr in adjList[vertix]:
            dfs(nighbr)
    
    for each in adjList.keys():
        if each not in visited:
            dfs(each)
            counts += 1

    print(counts)


if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
 
