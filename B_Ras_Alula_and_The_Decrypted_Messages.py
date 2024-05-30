def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        s = input()
        w = input()
        indx = 0 
        prfxSum = [0]
        targetSum = 0

        for char in s:
            prfxSum.append(prfxSum[-1] + ord(char))
        for char in w:
            targetSum += ord(char)

        ans = 'No'
        for i in range(m, n + 1):
            if prfxSum[i]  - prfxSum[i - m] == targetSum:
                ans = 'Yes'
                break

        print(ans)

if __name__ == '__main__':
    main()