def main():
    for _ in range(int(input())):
        n, t = map(int, input().split())
        dur = list(map(int, input().split()))
        val = list(map(int, input().split()))

        maxIndx = -1 

        for i in range(n):
            if dur[i] <= t:
                if maxIndx == -1 or val[maxIndx - 1] < val[i]:
                    maxIndx = i + 1
            t -= 1
        
        print(maxIndx)

if __name__ == '__main__':
    main()