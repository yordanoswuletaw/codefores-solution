from collections import defaultdict
def subSolution(arr, n):
    hashMap = defaultdict(int)
    start = 0
    while start < n:
        end = start + 1
        while end < n and arr[end] == arr[start]:
            end += 1
        hashMap[arr[start]] = max(hashMap[arr[start]], end - start)
        start = end
    return hashMap
    
def main():
    for _ in range(int(input())):
        n = int(input())
        arrA = list(map(int, input().split()))
        arrB = list(map(int, input().split()))
        hashMapA = subSolution(arrA, n)
        hashMapB = subSolution(arrB, n)
     
        ans = 0
        for i in range(n):
            ans = max(ans, hashMapA[arrA[i]] + hashMapB[arrA[i]], hashMapB[arrB[i]] + hashMapA[arrB[i]])
        
        print(ans)

if __name__ == '__main__':
    main()