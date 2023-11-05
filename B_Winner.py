from collections import defaultdict

def main():
    n = int(input())

    ans, hashMap = None , defaultdict(lambda: (0, float('inf'), float('inf')))
    for i in range(n):
        name, score = input().split()
        score = int(score)
        if score > 0:
            hashMap[name] = (hashMap[name][0] + score, score,  i)
        else:
            if hashMap[name][1] < abs(score):
                hashMap[name] = (hashMap[name][0] + score, i)
            else:
                hashMap[name] = (hashMap[name][0] + score, min(hashMap[name][0], i))


    maxVal = float('-inf')
    for key, val in hashMap.items():
        maxVal = max(maxVal, val[0])

    for key, val in hashMap.items():
        if val[0] == maxVal:
            if ans is None or ans[1] >= val[2]:
                ans = (key, val[2])
    
    print(ans[0])

if __name__ == '__main__':
    main()