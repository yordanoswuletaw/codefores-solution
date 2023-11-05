def main():
    n, k = map(int, input().split())
    remTime = 240 - k
    count = contestTime = 0
    for i in range(1, n + 1):
        contestTime += i * 5
        if contestTime > remTime:
            break
        count += 1
    
    print(count)

if __name__ == '__main__':
    main()