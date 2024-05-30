import sys, threading
from collections import Counter, defaultdict
input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    freq = Counter(nums)
    max_point = max(freq.keys())
    memo = defaultdict(int)
    def dp(point):
        if point > max_point:
            return 0
        if point not in memo:
            memo[point] = max(point * freq[point] + dp(point + 2), dp(point + 1))
        return memo[point]

    print(dp(0))
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
 
 