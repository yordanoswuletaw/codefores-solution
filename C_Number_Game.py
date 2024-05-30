def powerOfTwo(n):
    if n == 1:
        return True 
    if n % 2:
        return False
    return powerOfTwo(n // 2)

def main():
    for _ in range(int(input())):
        n = int(input())
        ans = False 
        while n > 1:
            if n % 2:
                ans = not ans 
                break
            if powerOfTwo(n):
                ans = not ans 
                n -= 1
            else:
                curr = 1
                for m in range((n // 2), 1, -1):
                    if n % m == 0 and m % 2:
                        curr = m 
                        if (n // curr) != 2:
                            break       
                n //= curr 
                ans = not ans
        if ans:
            print('Ashishgup')
        else:
            print('FastestFinger')

if __name__ == '__main__':
    main()