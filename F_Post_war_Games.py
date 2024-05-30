def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == n:
            print(0)
        else: 
            # win 
            ans = (n - (k + 1))*3 + ((k - 1)//2)*3 + (k - 1)%2 + 1
            ans = (n - (k + 1)) * 3 + k
            print(ans)

if __name__ == '__main__':
    main()