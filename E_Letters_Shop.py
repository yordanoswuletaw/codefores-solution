from collections import defaultdict, Counter

def main():
    n = int(input())
    letters = list(input())
    hashMap = defaultdict(list)
    for i in range(n):
        hashMap[letters[i]].append(i)
    t = int(input())
    names = []
    for _ in range(t):
        names.append(list(input()))
    
    result = []
    for each in names:
        currMax = float('-inf')
        nameMap = Counter(each)
    
        for key, val in nameMap.items():
            if val > 1:
                currMax = max(currMax, hashMap[key][val - 1])
            else:
                currMax = max(currMax, hashMap[key][0])
        result.append(currMax + 1)
    
    for each in result:
        print(each)
            
    
    

if __name__ == '__main__':
    main()

