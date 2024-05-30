from collections import defaultdict

class UnionFind:
    def __init__(self, perms, size):
        self.root = [i for i in range(size)]
        self.score = perms.copy()
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
                self.score[rootX] += self.score[rootY]
                return self.score[rootX]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
                self.score[rootY] += self.score[rootX]  
                return self.score[rootY]
        else:
            return self.score[rootX]

def main():
    n = int(input())
    perms = list(map(int, input().split()))
    orders = list(reversed([each - 1 for each in map(int, input().split())]))
    build = [0] * n 
    unionFind = UnionFind(perms, n)
    ans = []
    maxSum = 0 
    for order in orders:
        ans.append(maxSum)
        build[order] = 1
        left, right = order - 1, order + 1
        rep = unionFind.find(order)
        currMax = unionFind.score[rep]
        if left >= 0 and build[left]:
            currMax = unionFind.union(order, left)
        if right < n and build[right]:
            currMax = unionFind.union(order, right)
        maxSum = max(maxSum, currMax)

    for each in reversed(ans):
        print(each)

if __name__ == '__main__':
    main() 