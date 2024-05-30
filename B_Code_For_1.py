from math import ceil
def main():
    n, l, r = map(int, input().split())
    onesPos = set()

    def findOnesPos(next, num):
        if next <= 1:
            if next == 1:
                onesPos.add(1)
            if next == 1 and num == 1:
                onesPos.add(2)
            elif num == 1:
                onesPos.add(1)
            return 2
        power = findOnesPos(next // 2, next % 2)
        if num % 2:
            onesPos.add(2 ** power)
        return power + 1
    
    findOnesPos(n // 2, n % 2)
    ans = 0
    for i in range(l, r + 1):
        for each in onesPos:
            step = each * 2
            if i == each or (i - each) % step == 0:
                ans += 1
                break
    print(ans)

if __name__ == '__main__':
    
    main()
 
