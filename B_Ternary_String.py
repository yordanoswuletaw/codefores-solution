



from collections import defaultdict
for _ in range(int(input())):
    string = list(input())
    n = len(string)
    left = right = 0
    shortLen = 0
    hashMap = defaultdict(int)
    chars = set("123")
    while right < n:
        hashMap[string[right]] += 1
        right += 1
        while chars == set(hashMap.keys()):
            hashMap[string[left]] -= 1
            if hashMap[string[left]] == 0:
                if shortLen == 0:
                    shortLen = right - left
                else:
                    shortLen = min(shortLen, right - left)
                hashMap.pop(string[left])
            left += 1
    print(shortLen)
    
