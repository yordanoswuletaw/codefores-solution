def solution(cells, n, t):
    
    indx = 1
    while indx < n:
        if indx == t:
            return 'YES'
        indx += cells[indx - 1]
        
    
    if indx == t == n:
        return 'YES'

    return 'NO' 

def main():
    n, t = map(int, input().split())
    cells = list(map(int, input().split()))
    print(solution(cells, n, t))
    
if __name__ == '__main__':
    main()

