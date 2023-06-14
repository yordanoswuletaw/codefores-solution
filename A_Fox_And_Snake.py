from collections import defaultdict, deque

def main():
    n, m = map(int, input().split()) 

    pic = []
    end = True
    for i in range(n):
        if i % 2 == 0:
            pic.append('#' * m)
        else:
            if end:
                pic.append('.' * (m - 1) + '#')
            else:
                pic.append('#' + '.' * (m - 1))
            end = not end 
    
    for row in pic:
        print(row)

if __name__ == '__main__':
    main()