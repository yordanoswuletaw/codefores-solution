import sys, threading
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()


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
 
