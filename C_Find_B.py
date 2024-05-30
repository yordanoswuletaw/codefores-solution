def main():
    for _ in range(int(input())):
        n, q = map(int, input().split()) 
        nums = list(map(int, input().split()))
        prfxDiff = [0]
        for num in nums:
            prfxDiff.append(num + prfxDiff[-1])
       
        for _ in range(q):
            left, right = map(int, input().split())
            if left == right:
                print('NO')
            elif prfxDiff[right] - prfxDiff[left - 1] > :
                print('YES')
            else:
                print('NO')

if __name__ == '__main__':
    main() 