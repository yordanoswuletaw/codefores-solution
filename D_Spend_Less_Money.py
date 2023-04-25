def main():
    n, k = map(int, input().split())
    kow = list(map(int, input().split()))
    after = list(map(int, input().split()))

    all, money = [], 0

    for i in range(n):
       all.append((kow[i], after[i]))
    
    all.sort(key=lambda each: each[0] - each[1])

    for each in all:
        if k > 0:
            money += each[0]
        else:
            money += min(each)
        k -= 1
    
    print(money)
    
    
if __name__ == '__main__':
    main()

