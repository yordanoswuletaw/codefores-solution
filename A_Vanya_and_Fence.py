def main():
    n, h = map(int, input().split())
    heights = list(map(int, input().split()))

    res = 0
    for height in heights:
        if height > h:
            res += 2
        else:
            res += 1
    print(res) 

if __name__ == '__main__':
    main()