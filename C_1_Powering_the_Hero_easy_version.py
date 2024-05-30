def main():
    for _ in range(int(input())):
        n = int(input())
        deck = list(map(int, input().split()))
        bonusStack = []
        totArmy = 0
        
        for power in deck:
            if power:
                bonusStack.append(power)
                bonusStack.sort()
            else:
                if bonusStack:
                    totArmy += bonusStack.pop()
        
        print(totArmy)

if __name__ == '__main__':
    main()