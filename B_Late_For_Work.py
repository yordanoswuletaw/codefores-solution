def main():
    for _ in range(int(input())):
        n, currLight = input().split()
        n = int(n)
        lights = list(input())
        ans = 0
        prev = lights.index('g')
        i = 0
        while i < n:
            if lights[i] == 'g':
                i += 1
            elif lights[i] == currLight:
                j = i
                count = 0
                while j < n and lights[j] != 'g':
                    count += 1
                    if j == n - 1:
                        count += prev
                    j += 1
                ans = max(ans, count)
                i = j
            else:
                i += 1
            
        
        print(ans)

if __name__ == '__main__':
    main()