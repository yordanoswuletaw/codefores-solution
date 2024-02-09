from collections import defaultdict
def main():
    for _ in range(int(input())):
        input()
        input()
        n, m = map(int, input().split())
        nums = list(map(int, input().split()))
        queries = []
        for _ in range(m):
            queries.append(tuple(map(int, input().split()))) 
        
        intervals = defaultdict(lambda: (float('inf'), float('-inf')))
        for i in range(n):
            x, y  = intervals[nums[i]]  
            intervals[nums[i]] = (min(x, i), max(y, i))
        for x, y in queries:
            if intervals[x][0] < intervals[y][1]:
                print("YES")
            else:
                print("NO")

if __name__ == '__main__':
    main()

    