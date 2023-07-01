def main():
    n = int(input())
    m = int(input())
    taken = []
    for _ in range(n):
        taken.append(int(input()))
    taken.sort()
    maxVal = taken[-1] + m 
    for i in range(n):
        if m > 0:
            m -= taken[-1] - taken[i]
    
    minVal = taken[-1] 
    if m > 0:
        minVal +=  m // n + min(m % n, 1)
        
    print(minVal, maxVal)

if __name__ == '__main__':
    main()