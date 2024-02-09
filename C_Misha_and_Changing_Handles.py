def main():
    n = int(input())
    hashMap = {}
    key, value = set(), set()
    for _ in range(n):
        old, new = input().split()
        if old not in value:
            key.add(old)
        hashMap[old] = new 
        value.add(new)
    
    print(len(key))
    for old in list(key):
        new = hashMap[old]
        while new in hashMap:
            new = hashMap[new]
        print(old, new)

if __name__ == '__main__':
    main()