def main():
    n, m , k = map(int, input().split())

    array = list(map(int, input().split()))

    ops = []
    for _ in range(m):
        ops.append(list(map(int, input().split())))
    
    queries = []
    for _ in range(k):
        queries.append(list(map(int, input().split())))
    
    
    

if __name__ == '__main__':
    main()

