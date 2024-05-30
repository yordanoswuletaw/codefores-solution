from collections import defaultdict
def main():
    for _ in range(int(input())):
        n = int(input())
        N = 10 ** 5 + 5 
        nums = list(map(int, input().split()))
        nums.sort()

        dividers = [[] for _ in range(10 ** 5 + 10)]
        
        for i in range(N, 0, -1):
            for j in range(N, i-1, -i):
                dividers[i].append(j)
        
        hashMap = defaultdict(int)
        ans = 0
        for i in range(n):
            secondHash = defaultdict(int)
            num = nums[i]
            for divider in dividers[num]:
                if divider in hashMap:
                    count = (hashMap[divider] - secondHash[divider]) * divider * (n - i - 1)
                    ans += count 
                    hashMap[divider] += 1 
                    for val in dividers[divider]:
                        secondHash[val] += 1
                else:
                    hashMap[divider] += 1
               
        print(ans)


if __name__ == '__main__':
    main()