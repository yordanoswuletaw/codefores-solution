for _ in range(int(input())):

    n, s, r = map(int, input().split())
    seq = []
    res = r // (n - 1)
    rem = r % (n - 1)
    seq.append(s - r)
    for _ in range(n - 1):
        currSeq = res + rem 
        if currSeq > (s - r):
            rem = currSeq - (s - r)
            currSeq = (s - r)
        else:
            rem = 0
        seq.append(currSeq)
    print(*seq)
