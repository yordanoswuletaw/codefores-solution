from math import ceil
def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        demand = list(map(int, input().split()))
        pos = list(map(int, input().split()))   

        ans = float('inf')
        left, right = 1, max(demand)
        while left <= right:
            mid = left + (right - left) // 2
            currAns = 0 
            for i in range(n):
                turn = ceil(demand[i] / mid)
                currAns += 2 * turn + pos[i] * (2 * turn)
                
            if currAns <= k:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        if ans == float('inf'):
            print(-1)
        else:
            print(ans)


if __name__ == '__main__':
    main()
    '''
    bcvb
    adwa
    1-11-1
    '''