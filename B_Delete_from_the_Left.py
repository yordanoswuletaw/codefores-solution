def main():
    s1, s2 = input(), input()
    n, m = len(s1), len(s2)
    moves = abs(n - m)
    if n > m:
        s1 = s1[n - m:]
    elif n < m:
        s2 = s2[m - n:]
    
    n = min(n, m)
    for i in range(n - 1, -1, -1):
        if s1[i] != s2[i]:
            moves += (n - (n - 1 - i)) * 2
            break
    print(moves)

if __name__ == '__main__':
    main()