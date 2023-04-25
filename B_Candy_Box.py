from collections import Counter

import sys, threading

input = lambda: sys.stdin.readline().strip()


def main():
     for _ in range(int(input())):
        n = int(input())
        
        nums = sorted(Counter(map(int, input().split())).values(), reverse=True )
        maxSize = nums[0]
        currSize = maxSize - 1

        for i in range(1, len(nums)):
            if currSize <= 0:
                break
            currSize = min(currSize, nums[i])
            maxSize += currSize
            currSize -= 1
        
        print(maxSize)
    


if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()



