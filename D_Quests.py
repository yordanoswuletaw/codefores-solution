from math import floor

def main():
    for _ in range(int(input())):
        n, c, d = map(int, input().split())
        quests = sorted(map(int, input().split()), reverse=True)
        if quests[0] * d < c:
            print('Impossible')
        elif quests[0] > c:
            print('Infinity')
        else:
            k = float('inf')
            left, right = 1, d 
            while left <= right:
                mid = left + (right - left) // 2
                tot = 0
                for i in range(min(d // mid, n)):
                    tot += quests[i] * mid
                if tot >= c:
                    k = min(k, mid)
                    right = mid - 1
                else:
                    left = mid + 1
            print(k)


if __name__ == '__main__':
    main()