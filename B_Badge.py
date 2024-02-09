def main():
    n = int(input())
    p = list(map(int, input().split()))

    ans = [0] * n 
    for i in range(n):
        memo = [0] * n
        memo[i] = 1
        j = p[i] -1
        while memo[j] < 2:
            memo[j] += 1
            j = p[j] - 1
        ans[i] = j + 1
    print(*ans)

if __name__ == '__main__':
    main()