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

def main():
    for _ in range(int(input())):
        n = int(input())
        unionFind = UnionFind(n)
        nodes = list(map(int, input().split()))
        maxNode = nodes[0]
        for indx in range(1, n):
            maxNode = max(maxNode, nodes[indx])
            if maxNode <= indx + 1:
                continue
            unionFind.union(nodes[indx] - 1, maxNode - 1) 
        
        components = set()
        for i in range(n):
            components.add(unionFind.find(i))

        print(len(components))


if __name__ == '__main__':
    main()