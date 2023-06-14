from collections import defaultdict
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest

def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        boards = list(map(int, input().split()))
        heapify(boards)
        ops = list(map(int, input().split()))

        for i in range(m):
            heappop(boards)
            heappush(boards, ops[i])
        
        print(sum(boards))

if __name__ == '__main__':
    main()