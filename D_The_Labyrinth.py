import sys, threading

input = lambda: sys.stdin.readline().strip()


def main():
    n, m = map(int, input().split())
    
    graph = []
    dir = [(-1,0),(1,0),(0,1),(0,-1)]

    for i in range(n):
        graph.append(list(input()))
    
    empties, impos = [], []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '.':
                empties.append((i,j))
            else:
                impos.append((i,j))

    connecteds = []
    visited = set()

    def outBound(i, j):
        if i < 0 or i >= n or j < 0 or j >= m or  (i, j) in visited or graph[i][j] == '*':
            return True 

    def dfs(i, j, group):
        if outBound(i, j):
            return group
        group.add((i, j))
        visited.add((i, j))
        for x, y in dir:
            newx = i + x 
            newy = j + y 
            dfs(newx, newy, group)
        
        return group

    for i,j in empties:
        if (i, j) not in visited:
            connecteds.append(dfs(i, j, set()))
    
    ans = graph.copy()
    def inBound(i, j, visited):
        if 0 <= i < n and 0 <= j < m and graph[i][j] == '.' and (i, j) not in visited:
            return True 

    for i,j in impos:
        ans[i][j] = 1
        visited = set()
        for x, y in dir:
            newx = i + x 
            newy = j + y 
            if inBound(newx, newy, visited):
                for each in connecteds:
                    if (newx, newy) in each:
                        for vr in each:
                            visited.add(vr)
                        ans[i][j] += len(each)
        ans[i][j] %= 10

    for each in ans:
        print(''.join(map(str, each)))

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
 
