def main():
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        mx, mn = max(a, b), min(a, b)
        ans = 0
        while mx > mn:
            ans += 1
            mn += c 
            mx -= c 
        print(ans)

if __name__ == '__main__':
    main()