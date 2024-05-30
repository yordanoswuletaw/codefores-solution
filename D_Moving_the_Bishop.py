from collections import deque
def main():
    n = int(input())
    sx, sy = map(int, input().split())
    sx, sy = sx - 1, sy - 1
    ex, ey = map(int, input().split())
    ex, ey = ex - 1, ey - 1

    board = []
    for _ in range(n):
        board.append(list(map(lambda x: x if x == '#' else float('inf'), list(input()))))
    
    direc = {(-1, -1): 'LU', (1,1): 'RD', (1, -1): 'LD', (-1, 1): 'RU'}
   
    queue = deque([(sx, sy, 'CENTER')])
    board[sx][sy] = 0

    def inbound(x, y, move):
        return 0 <= x < n and 0 <= y < n and board[x][y] != '#' and board[x][y] > move
    
    while queue: 
        x, y, path = queue.popleft()
        if (x, y) == (ex, ey):
            print(board[x][y])
            return
       
        for dx, dy in direc.keys():
            _x, _y = x + dx, y + dy
            new_path = direc[(dx, dy)]
            move = board[x][y] + int(new_path != path)
            if inbound(_x, _y, move):
                queue.append((_x, _y, new_path))
                board[_x][_y] = move
    
    print(-1)
    
if __name__ == '__main__':
    main()
 
 