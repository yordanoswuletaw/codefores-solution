






import sys, threading
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()
n, m = map(int, input().split())
catsV = list(map(int, input().split()))

adjSet = defaultdict(list)

def dfs(parent, childrens, count):
    if not childrens:
        if count > m:
            if catsV[parent - 1] and catsV[catsV[parent - 1]]:
                return 0
        return 1
    currSum = 0
    for child in childrens:
        if catsV[child - 1]:
            if count + catsV[child - 1] > m:
                return 0
        else:
            count = 0
        currSum += dfs(child, adjSet[child], count + catsV[child - 1])
    return currSum

def main():
    for _ in range(n - 1):
        parent, child = map(int, input().split())
        adjSet[parent].append(child)


    currSum = 0
    for child in adjSet[1]:
        currSum += dfs(child, adjSet[child], catsV[0] + catsV[child - 1])

    print(currSum)

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()






    

