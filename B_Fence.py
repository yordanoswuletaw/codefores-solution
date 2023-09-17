def main():
    n, k = map(int, input().split())
    fence = list(map(int, input().split()))

    for i in range(1, n):
        fence[i] += fence[i - 1]
    
    k -= 1
    indx, currSum = 1, fence[k]
    for i in range(1, n - k):
        if currSum > fence[i + k] - fence[i - 1]:
            currSum = fence[i + k] - fence[i - 1]
            indx = i + 1
    
    print(indx)


if __name__ == '__main__':
    main()