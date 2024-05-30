from collections import Counter
from sys import stdin
def main():
    for _ in range(int(input())):
        n = int(input())
        candies = Counter(map(int, stdin.readline().split()))
        candies = sorted(candies.values(), reverse=True)
        ans = 0
        reminder = 0
        prev = float('inf')
        for val in candies:
            if val > prev:
                ans += prev 
                prev -= 1
            else:
                ans += val 
                prev = val - 1
            if prev <= 0:
                break
        print(ans)
if __name__ == '__main__':
    main()