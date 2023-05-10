def main():
    n = 2 * 10 ** 5 + 1
    bitSums = [[0] * 20 for _ in range(n)]
    for i in range(1, n):
        for j in range(20):
            bit = 1
            if i & (1 << j):
                bit = 0
            bitSums[i][j] = bitSums[i - 1][j] + bit
   
    for _ in range(int(input())):
        l, r = map(int, input().split())
     
        minNum = float('inf')
        for i in range(20):
            minNum = min(bitSums[r][i] - bitSums[l - 1][i], minNum)
        print(minNum)

if __name__ == '__main__':
    main()

