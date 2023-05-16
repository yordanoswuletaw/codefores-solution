def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        ans = 0

        for i in range(n):
            xor = 0
            for j in range(n):
                if i != j:
                    xor = xor ^ arr[j]
            if xor == arr[i]:
                ans = xor
                break

        print(ans)
    

if __name__ == '__main__':
    main()

