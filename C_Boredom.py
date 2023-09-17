from collections import Counter
def main():
    n = int(input())
    nums = list(map(int, input().split()))
    ans = sum(nums)
    hashMap =  Counter(nums)
    nums = [(num, freq) for num, freq in hashMap.items()]
    nums.sort(key=lambda x: x[0] * x[1], reverse=True)
    removed = set()
   
    for num, freq in nums:
        if num not in removed:
            removed.add(num) 
            if num - 1 not in removed:
                ans -= (num - 1) * hashMap[num - 1]
                removed.add(num - 1)
            if num + 1 not in removed:
                ans -= (num + 1) * hashMap[num + 1]
                removed.add(num + 1)

    print(ans)

if __name__ == '__main__':
    main()