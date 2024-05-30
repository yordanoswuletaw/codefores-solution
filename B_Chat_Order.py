from heapq import heapify, heappop

def main():
    n = int(input())
    hashMap = {}

    for i in range(n):
        friend = input()
        hashMap[friend] = [-i, friend]
    
    heap = list(hashMap.values())
    heapify(heap)
    while heap:
        time, friend = heappop(heap)
        print(friend)
    
if __name__ == '__main__':
    main()
 