def main():
    for _ in range(int(input())):
        n = int(input())
        cupcakes = list(map(int, input().split()))
        target = sum(cupcakes)
        currSum = start = 0
        ans = 'YES'
        for end in range(n):
            if start == 0 and end == n - 1:
                break
            currSum += cupcakes[end]
            if currSum <= 0:
                start = end + 1
                currSum = 0
            if currSum >= target:
                ans = 'NO'
                break
        
        if ans == 'YES':
            currSum = start = 0
            for end in range(1, n):
                currSum += cupcakes[end]
                if currSum <= 0:
                    start = end + 1
                    currSum = 0
                if currSum >= target:
                    ans = 'NO'
                    break 
        print(ans)

if __name__ == '__main__':
    main()