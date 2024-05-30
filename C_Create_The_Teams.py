from math import ceil
def main():
    for _ in range(int(input())):
        n, x = map(int, input().split())
        teams = list(map(int, input().split()))
        teams.sort(reverse=True)
        teams = [(team, ceil(x / team)) for team in teams]
        
        ans = 0
        start = 0
        while start < n:
            count = teams[start][1]
            if count < 1:
                ans += 1
                start += 1
            else:
                end = start 
                while end < n and count > end - start + 1:
                    end += 1
                    if end < n:
                        count = teams[end][1]
                if end < n:
                    ans += 1
                start = end + 1
        print(ans)

if __name__ == '__main__':
    main()