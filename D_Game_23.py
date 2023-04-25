import sys, threading

input = lambda: sys.stdin.readline().strip()

# solution 1: using recursion
class Transform:
    def __init__(self):
        self.moves = 0
        self.found = False
        self.hashSet = set()

    def transform(self, n, m, moves):
        if n == m:
            self.moves = moves
            self.found = True 
            return 
        if n > m or self.found:
            if not self.found:
                self.moves = -1
            return 
        if n * 2 not in self.hashSet:
            self.hashSet.add(n * 2)
            self.transform(n * 2, m, moves + 1)
        if n * 3 not in self.hashSet:
            self.hashSet.add( n * 3)
            self.transform(n * 3, m, moves + 1)

# solution 2: using math
def transform(n, m):
    if m % n:
        return -1
    q = m // n
    count = 0
    while q != 1:
        if q % 2 and q % 3:
            return -1
        elif q % 2:
            q //= 3
        else:
            q //= 2
        count += 1
    return count


def main():
    n, m = map(int, input().split())
    t = Transform()
    t.transform(n, m, 0)
    #print(t.moves)
    print(transform(n, m))
    


if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

