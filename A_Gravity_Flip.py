def main():
    n = int(input())
    cubes = map(int, input().split())

    print(*sorted(cubes)) 

if __name__ == '__main__':
    main()