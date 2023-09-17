def main():
    for _ in range(int(input())):
        n = int(input())
        perms = list(map(int, input().split()))

        node = components = 0
        for i in range(n):
            node = max(node, perms[i])
            if node <= i + 1:
                components += 1
        
        print(components)

if __name__ == '__main__':
    main()