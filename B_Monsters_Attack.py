def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        a = list(map(int, input().split())) 
        x = list(map(int, input().split())) 

        left, right = [], []
        for i in range(n):
            if x[i] < 0:
                left.append((abs(x[i]), a[i]))
            else:
                right.append((x[i], a[i]))
        
        maxLen = max(max(x), abs(min(x))) + 1
        totHealth = [0] * maxLen
        for i, health in left:
            totHealth[i] += health
        for i, health in right:
            totHealth[i] += health
        
        gun = 0
        ans = 'YES'
        for health in totHealth:
            if gun < health:
                ans = 'NO'
                break 
            gun -= health
            gun += k 
        
        print(ans)
        
        

if __name__ == '__main__':
    main() 