for _ in range(int(input())):
    n = int(input())
    seq = list(map(int, input().split()))
    res = []
    i, j = 0, n - 1
    while i <= j:
        res.append(seq[i])
        if i != j:
            res.append(seq[j])
        i += 1
        j -= 1
    print(*res)