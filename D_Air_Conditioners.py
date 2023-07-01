def main():
    for _ in range(int(input())):
        input()
        n, k = map(int, input().split())
        indecies = list(map(int, input().split()))
        forward = [float('inf')] * n


        for i, temp in enumerate(map(int, input().split())):
            forward[indecies[i] - 1] = temp 
        
        backward = forward[:]
        for i in range(1, n):
            if forward[i - 1] != float('inf'):
                forward[i] = min(forward[i], forward[i - 1] + 1)
            if backward[n - i] != float('inf'):
                backward[n - i - 1] = min(backward[n - i - 1], backward[n - i] + 1)
        
        ans = []
        for i in range(n):
            ans.append(min(forward[i], backward[i]))
        
        print(*ans)

if __name__ == '__main__':
    main()