from collections import defaultdict

def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    hashMap = defaultdict(int)
    for num in nums:
        hashMap[num] += 1
    
    dists = []

    for i in range(n):
        dists.append(len(hashMap))
        hashMap[nums[i]] -= 1
        if hashMap[nums[i]] <= 0:
            hashMap.pop(nums[i])

    
    for _ in range(m):
        l = int(input()) - 1
        print(dists[l])
            

if __name__ == '__main__':
    main()

