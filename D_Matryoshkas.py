from collections import Counter

for _ in range(int(input())):
    n = int(input())
    dolls = Counter(map(int, input().split()))
    res = 0
    maxIter = max(dolls.values())
    for _ in range(maxIter):
        nest = 0
        for i, key in enumerate(sorted(dolls.keys())):
            if i > 0 and (key - 1 not in dolls or dolls[key] == 0):
                res += nest
                nest = 0
            if dolls[key]:
                nest = 1
                dolls[key] -= 1
        res += nest

    print(res)

