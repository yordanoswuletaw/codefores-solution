def main():
    n = int(input())
    nums = list(map(int, input().split()))

    expected = sum(nums) // n
    diff = [num - expected for num in nums]
    
    moves = 0
    ptv = ntv = 0
    
    while ntv < n:
        while diff[ntv] < 0:
            while ptv < n and diff[ptv] <= 0:
                ptv += 1
            move = min(abs(diff[ntv]), diff[ptv])
            moves += abs(ptv - ntv) * move
            diff[ntv] += move
            diff[ptv] -= move

        ntv += 1
    
    print(moves)

if __name__ == '__main__':
    main()