from math import gcd

def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))

        if n == 1:
            print(0)
            continue

        for i in range(n):
            nums[i] -= k 
        
        ptv = zero = neg = 0
        for num in nums:
            if num > 0:
                ptv += 1
            elif num == 0:
                zero += 1
            else:
                neg += 1 
        
        if ptv == n:
            m = nums[0]
            for num in nums[1:]:
                m = gcd(m, num)
            ans = 0
            for num in nums:
                ans += (num // m) - 1
            print(ans) 
        elif neg == n:
            m = -nums[0]
            for num in nums[1:]:
                m = -gcd(m, -num) 
            ans = 0
            for num in nums:
                ans += (num // m) - 1
            print(ans) 
        elif zero == n:
            print(0)
        else:
            print(-1)

if __name__ == '__main__':
    main()