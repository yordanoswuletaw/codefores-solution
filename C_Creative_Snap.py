import sys, threading
from collections import Counter
from bisect import bisect_left, bisect_right
input = lambda: sys.stdin.readline().strip()

def main():
    n, k, A, B = map(int, input().split())
    avengers = sorted(map(int, input().split()))
    hashMap = Counter(avengers)
    def dq(l, r):
        if l == r: 
            if l in hashMap:
                return B 
            else:
                return A
        right = bisect_right(avengers, r) 
        left = bisect_left(avengers, l)
        if right - left == 0:
            return A

        currAns = B * (right - left) * (r - l + 1)
        m = (l + r) // 2
        currAns = min(currAns, dq(l, m) + dq(m + 1, r))
        return currAns


    print(dq(1, 2 ** n))     
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
 
