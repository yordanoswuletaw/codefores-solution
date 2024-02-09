def main():
    strings = list(input())     
    n = int(input())
    queries = []
    for _ in range(n):
        queries.append(list(map(int, input().split())))

    prefixSum = [0] * len(strings)
    for i in range(1, len(strings)):
        if strings[i] == strings[i - 1]:
            prefixSum[i] = prefixSum[i - 1] + 1
        else:
            prefixSum[i] = prefixSum[i - 1]
    
    for query in queries:
        l, r = query
        print(prefixSum[r - 1] - prefixSum[l - 1])

if __name__ == '__main__':
    main()