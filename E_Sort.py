def solution(arr, n):
    result = []
    indx = 1
    while indx < n:
        if arr[indx] >= arr[indx - 1]:
            result.append(arr[indx - 1])
            result.append(arr[indx])
        else:
            result.append(arr[indx])
            result.append(arr[indx - 1])
        indx += 2

    if n % 2:
        result.append(arr[-1])

    p1, p2 = 0, 1
    while p2 < n:
        if result[p2] < result[p1]:
            return 'NO'
        p1 += 1
        p2 += 1
    
    return 'YES'
    

def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))

        print(solution(arr, n))
    

if __name__ == '__main__':
    main()

