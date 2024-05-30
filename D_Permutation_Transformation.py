def main():
    for _ in range(int(input())):
        n = int(input())
        perms = list(map(int, input().split()))
        ans = [0] * n
        
        def helper(l, r, depth):
            if l > r:
                return
            maxVal = max(perms[l:r+1])
            maxIndex = perms.index(maxVal)
            ans[maxIndex] = depth
            helper(l, maxIndex-1, depth+1)
            helper(maxIndex+1, r, depth+1)

        helper(0, n-1, 0)
        
        print(*ans)

if __name__ == '__main__':
    main()