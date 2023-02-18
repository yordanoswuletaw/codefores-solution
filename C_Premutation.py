    for _ in range(int(input())):
        
        n = int(input())
        perms = []
        dict = {}
        for _ in range(n):
            perms.append(list(map(int, input().split())))
        for i in range(n):
            for j in range(n - 1):
                dict[perms[i][j]] = dict.get(perms[i][j], 0) + ((n - j) ** 2)
        
        print(' '.join(map(str, sorted(dict, key=lambda x: dict[x], reverse=True))))