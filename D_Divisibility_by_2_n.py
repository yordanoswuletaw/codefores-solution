from math import lcm
def main():
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))

        product = 1
        for num in nums:
            product *= num 
        
        num = lcm(product, 2 ** n) // product
        count = 0
        while num > 1 and n > 0:
            if num % n == 0:
                num //= n 
                count += 1
            n -= 1
        
        if num <= 1:
            print(count)
        else:
            print(-1)


if __name__ == '__main__':
    main()

