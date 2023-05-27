import sys, threading
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())
    vertices = list(input() for _ in range(n))
    edges = [(tuple(input().split())) for _ in range(m)]

    teams = []

    def dfs(indx, currSet):
        nonlocal teams
        if indx >= n:
            return 
        for i in range(indx, n):
            currSet.add(vertices[i])
            getOnWell = all(a not in currSet or b not in currSet for a, b in edges)
            if getOnWell and len(currSet) > len(teams):
                teams = list(currSet)
            dfs(i + 1, currSet)
            currSet.remove(vertices[i])

    dfs(0, set())
    teams.sort()
    print(len(teams))
    for team in teams:
        print(team)


if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
 
