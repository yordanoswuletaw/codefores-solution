t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = ['a'] * n
    for i in range(n - 2, -1, -1):
        if k <= (n - i - 1):
            s[i] = 'b'
            s[n - k] = 'b'
            print("".join(s))
            break
        k -= (n - i - 1)
