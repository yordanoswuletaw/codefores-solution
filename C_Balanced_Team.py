def main():
    n = int(input())
    skills = sorted(map(int, input().split()))

    maxNum = 0
    end = 0

    for start in range(n):

        while end < n and skills[end] - skills[start] <= 5:
            end += 1
        maxNum = max(maxNum, end - start)

    print(maxNum)

if __name__ == '__main__':
    main()
