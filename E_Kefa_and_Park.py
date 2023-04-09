import sys, threading
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
catsV = list(map(int, input().split()))

adjSet = defaultdict(list)

def dfs(node, prevConsec, parent):

    prevConsec += catsV[node - 1]
    if prevConsec > m:
        return 0
    if not catsV[node - 1]:
        prevConsec = 0
    
    if adjSet[node] == [parent]:
        return 1
    
    paths = 0
    for child in adjSet[node]:
        if child != parent:
            paths += dfs(child, prevConsec, node)

    return paths
  

def main():
    for _ in range(n - 1):
        parent, child = map(int, input().split())
        adjSet[parent].append(child)
        adjSet[child].append(parent)

    print(dfs(1, 0, -1))

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
