def getGCF(num1, num2):
    if num2 == 0:
        return num1 
    return getGCF(num2 , num1 % num2)
def main():
    for _ in range(int(input())):
        n = int(input())
        hashMap = {num: i for i, num in enumerate(map(int, input().split()))}

        maxVal = -1
        for num1 in list(hashMap.keys()):
            for num2 in list(hashMap.keys()):
                if getGCF(max(num1, num2), min(num1, num2)) == 1:
                    maxVal = max(maxVal, hashMap[num1] + hashMap[num2] + 2)

        print(maxVal)

if __name__ == '__main__':
    main()

