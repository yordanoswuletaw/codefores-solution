def main():
    n = int(input())
    cities = list(map(int, input().split()))

    minDist = min(cities)
    if cities.count(minDist) > 1:
        print('Still Rozdil')
    else:
        print(cities.index(minDist) + 1)

if __name__ == '__main__':
    main()