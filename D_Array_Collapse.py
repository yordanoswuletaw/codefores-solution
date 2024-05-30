MOD = 998244353

def normalize(x):
    x %= MOD
    if x < 0:
        x += MOD
    return x

def main():
    
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        
        nextMin = [0] * n
        dpSum = [0] * (n + 2)
        dpNext = [0] * n
        
        stMin = []
        nextMin[n - 1] = n
        dpSum[n] = 1
        
        for pos in range(n - 1, -1, -1):
            while stMin and a[stMin[-1]] > a[pos]:
                stMin.pop()
            nextMin[pos] = n if not stMin else stMin[-1]
            stMin.append(pos)
            
            nxtPos = nextMin[pos]
            dpPos = normalize(dpSum[pos + 1] - dpSum[nxtPos + 1])
            print('mmmm', nxtPos, dpPos)
            if nxtPos != n:
                dpPos = normalize(dpPos + dpNext[nxtPos])
                dpNext[pos] = normalize(dpSum[nxtPos] - dpSum[nxtPos + 1] + dpNext[nxtPos])
            dpSum[pos] = normalize(dpPos + dpSum[pos + 1])
            
        res = 0
        mn = a[0]
        for i in range(n):
            mn = min(mn, a[i])
            if a[i] == mn:
                res = normalize(res + dpSum[i] - dpSum[i + 1])
        print(res)

if __name__ == "__main__":
    main()