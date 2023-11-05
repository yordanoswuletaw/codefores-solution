def solve(mat, n):
    for i in range(n - 1):
        for j in range(n - 1):
            if mat[i][j] and not mat[i + 1][j] and not mat[i][j + 1]:
                return 'NO'
    return 'YES'

def main():
    for _ in range(int(input())):
        n = int(input())
        mat = []
        for _ in range(n):
            mat.append([int(num) for num in input()])
        
        print(solve(mat, n))

if __name__ == '__main__':
    main()
