from collections import defaultdict, deque

def main():
    n, k = map(int, input().split())
    wallX = list(input())
    wallY = list(input())

    queue = deque()
    visited = set() 
    if wallX[0] == '-':
        queue.append((0, 'x'))
        visited.add((0, 'x'))
    if wallY[0] == '-':
        queue.append((0, 'y'))
        visited.add((0, 'y'))
    flX = flY = 0
    ans = 'No'

    while queue:
        indx, type = queue.popleft()
        if indx >= n - 1:
            ans = 'YES'
            break
        
        if type == 'x':
            if wallX[indx + 1] == '-':
                queue.append((indx + 1, type))
                visited.add((indx + 1, type))
            if indx - 1 >= 0 and wallX[indx - 1] == '-':
                queue.append((indx - 1, type))
                visited.add((indx - 1, type))
            if indx + k >= n:
                ans = 'YES'
                break 
            elif wallY[indx + k] == '-':
                queue.append((indx + k, 'y'))
                visited.add((indx + k, 'y'))
            wallX[flX] = 'X'
            flX += 1

        else:
            if wallY[indx + 1] == '-':
                queue.append((indx + 1, type))
                visited.add((indx + 1, type))
            if indx - 1 >= 0 and wallY[indx - 1] == '-':
                queue.append((indx - 1, type))
                visited.add((indx - 1, type))
            if indx + k >= n:
                ans = 'YES'
                break 
            elif wallX[indx + k] == '-':
                queue.append((indx + k, 'x'))
                visited.add((indx + k, 'x'))
            wallY[flY] = 'X'
            flY += 1
        
    print(ans)
            

if __name__ == '__main__':
    main()