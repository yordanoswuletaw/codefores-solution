def main():
    n, q = map(int, input().split())
    nums = sorted(map(int, input().split()), reverse=True)

    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))

    querySum = [0] * (n + 1) 
    for query in queries:
        querySum[query[0] - 1] += 1
        querySum[query[1]] -= 1
    
    for i in range(1, len(querySum)):
        querySum[i] += querySum[i - 1]

    querySum.sort(reverse=True)
    maxSum = 0
    for i in range(n):
        maxSum += querySum[i] * nums[i]
    
    print(maxSum)

if __name__ == '__main__':
    main()

