from collections import deque
import sys, threading

input = lambda: sys.stdin.readline().strip()

def solve(n, m):
    queue = deque([n])
    visited = set([n])
    minNum = 0

    while queue:
        for _ in range(len(queue)):
            currNum = queue.popleft()
            if currNum == m:
                return minNum
            
            num1 = currNum - 1
            num2 = currNum * 2
            if num2 not in visited and currNum <= 2 * m:
                queue.append(num2)
                visited.add(num2)
            if num1 not in visited and num1 > 0:
                queue.append(num1)
                visited.add(num1)
        minNum += 1
        
    return 0

def main():
    n, m = map(int, input().split())

    print(solve(n, m))
    


if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
 
