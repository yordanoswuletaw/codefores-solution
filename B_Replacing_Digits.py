def main():
    a = list(input())
    s = sorted(list(input()), reverse=True)

    n, m = len(a), len(s)
    i = j = 0
    while i < n and j < m:
        if a[i] < s[j]:
            a[i] = s[j]
            j += 1
        i += 1
    
    print(''.join(a))

if __name__ == '__main__':
    main()