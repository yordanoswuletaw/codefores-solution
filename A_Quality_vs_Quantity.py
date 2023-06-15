from collections import defaultdict
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest

def solution(nums, n):
    lSum, rSum = 0, 0
    left, right = 0, n - 1
    while left < right:
        if rSum <= lSum:
            rSum += nums[right]
            right -= 1
        elif left <= (n - right - 1):
            lSum += nums[left]
            left += 1
        if rSum > lSum and left > (n - right - 1):
            return 'YES'
    
    return 'NO'


def main():
    for _ in range(int(input())):
        n = int(input())
        nums = sorted(map(int, input().split()))
        print(solution(nums, n))


if __name__ == '__main__':
    main()