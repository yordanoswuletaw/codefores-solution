def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))

        bits = [0] * 31
        res = 0

        for num in nums:
            for i in range(31):
                if num & (1 << i):
                    bits[i] += 1
        
        for i in range(30, -1, -1):
            needed = n - bits[i]
            if needed <= k:
                k -= needed
                res += (1 << i)


        print(res)


if __name__ == '__main__':
    main()

