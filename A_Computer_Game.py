from collections import deque

def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        graph = []
        for _ in range(2):
            graph.append(list(map(int, input())))
        
        queue = deque([(0,0)])
        visited = set([(0, 0)])
        direc = [(1, 1), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1,-1), (-1, 1)]
        ans = 'NO'
        
        def inBound(x, y):
            if 0 <= x < 2 and 0 <= y < m and (x, y) not in visited and (graph[x][y] == 0 or  (x + y == m)):
                return True

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if x == 1 and y == m - 1:
                    ans = 'YES'
                    break
                for _x, _y in direc:
                    newX, newY = x + _x, y + _y 
                    if inBound(newX, newY):
                        queue.append((newX, newY))
                        visited.add((newX, newY))
        print(ans)


if __name__ == '__main__':

    main()
