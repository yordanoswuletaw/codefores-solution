import sys, threading

input = lambda: sys.stdin.readline().strip()

def solution(graph, good, bad, n, m):
    direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def inBound(x, y):
        if 0 <= x < n and 0 <= y < m and (x, y) not in visited and graph[x][y] != '#':
            return True

    def dfs(x, y):
        if x == n - 1 and y == m - 1 and graph[x][y] != '#':
            return True 
        if not inBound(x, y):
            return False
        
        visited.add((x, y))
        for i, j in direc:
            _x, _y = x + i, y + j
            if dfs(_x, _y):
                return True 

    for x, y in good:
        visited = set()
        if (x, y) not in visited:
            if not dfs(x, y):
                return 'No'
        visited.clear()
            
    for x, y in bad:
        visited = set()
        if (x, y) not in visited:
            if dfs(x, y):
                return 'No'
        visited.clear()
    
    return 'Yes'

def main():
    for _ in range(int(input())):
        n, m = map(int, input().split()) 
        graph = []
        good, empty, bad = [], [], []
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(n):
            graph.append(list(input()))
            for j, char in enumerate(graph[i]):
                if char == '.':
                    empty.append((i, j))
                if char == 'G':
                    good.append((i, j))
                if char == 'B':
                    bad.append((i, j))
    
        for x, y in empty:
            for i, j in direc:
                _x = x + i
                _y = y + j
                if 0 <= _x < n and 0 <= _y < m and graph[_x][_y] == 'B':
                    graph[x][y] = '#'

        print(solution(graph, good, bad, n, m))     

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()