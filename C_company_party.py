















import sys, threading
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()
adjSet = defaultdict(list)

def dfs(parents, count):
    if not parents:
        return count 
    maxCount = 0
    for child in parents:
        maxCount = max(maxCount, dfs(adjSet[child], count + 1))
    return maxCount

def main():
    n = int(input())
    employees = []

    for _ in range(n):
        employees.append(int(input()))

    for i in range(n):
        adjSet[employees[i]].append(i + 1)

    maxCount = 0

    for child in adjSet[-1]:
        maxCount = max(maxCount, dfs(adjSet[child], 1))

    print(maxCount)

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
