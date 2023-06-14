from collections import defaultdict, deque

def inBound(mazes, visited, n, m, x, y):
        if 0 <= x < n and 0 <= y < m and (x, y) not in visited and mazes[x][y] == '.':
            return True 

def bfs(mazes, empty, n, m, k):
    direc = ((1,0),(-1,0),(0,-1),(0,1))
    visited = set()
    for x,y in empty:
        if (x,y) in visited:
            continue
        queue = deque([(x,y)])
        visited.add((x,y))
        shouldEmpty = set([(x,y)])
        if len(shouldEmpty) == len(empty) - k:
            return shouldEmpty
        
        while queue:
            u, v = queue.popleft()
            for i, j in direc:
                _u = u + i 
                _v = v + j
                if inBound(mazes, visited, n, m, _u, _v):
                    visited.add((_u, _v))
                    shouldEmpty.add((_u, _v))
                    queue.append((_u,_v))
                    if len(shouldEmpty) == len(empty) - k:
                        return shouldEmpty
    return set()

def main():
    n, m, k = map(int, input().split()) 

    mazes = []
    for _ in range(n):
        mazes.append(list(input()))
    empty = []
    for i in range(n):
        for j in range(m):
            if mazes[i][j] == '.':
                empty.append((i, j))
    
    shouldEmpty = bfs(mazes, empty, n, m, k)
    for x, y in empty:
        if (x,y) not in shouldEmpty:
            mazes[x][y] = 'X'
    
    for row in mazes:
        print(''.join(row))
   
if __name__ == '__main__':
    main()