


import sys, threading

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())

# class Transform:
#     def __init__(self):
#         self.moves = 0
#         self.found = False
moves, found = 0, False
hashSet = set()
def transform(n, m, move):
    global found 
    global moves
    if n == m:
        moves = move
        found = True 
        return
    
    if n > m or found:
        if not found:
            moves = -1
        return
    if n * 2 not in hashSet:
        hashSet.add(n * 2)
        transform(n * 2, m, move + 1)
    if n * 3 not in hashSet:
        hashSet.add(n * 3)
        transform(n * 3, m, move + 1)
  

def main():
    #t = Transform()
    transform(n, m, 0)
    print(moves)

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

