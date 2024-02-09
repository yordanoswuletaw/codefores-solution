import sys 
def main():
    for _ in range(int(input())):
        n, q = map(int, input().split())
        inp = sys.stdin.readline()
        arr = [int(i) for i in inp.split()]
        prfxSum = [0] * (n + 1)
        for i in range(len(arr)):
            prfxSum[i + 1] = prfxSum[i] + arr[i]
        
        for i in range(q):
            start, end, num = map(int, input().split())
            res = prfxSum[-1] + (num * (end - start + 1)) - (prfxSum[end] - prfxSum[start - 1])
            if res % 2:
                print('YES')
            else:
                print('NO')
        
if __name__ == '__main__':
    main()