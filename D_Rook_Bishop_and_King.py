from collections import deque
def main():
    r1, c1, r2, c2 = map(int, input().split())

    rook = 0
    if r1 == r2 or c1 == c2:
        rook = 1
    else:
        rook = 2
    bishop = 0
    if (abs(r2 - r1) + abs(c2 - c1)) % 2:
        bishop = 0
    elif abs(r2 - r1) == abs(c2 - c1):
        bishop = 1
    else:
        bishop = 2
    king = 0 
    if r1 == r2:
        king = abs(c1 - c2)
    elif c1 == c2:
        king = abs(r1 - r2)
    elif abs(c2 - c1) == abs(r2 - r1):
        king = abs(c2 - c1)
    else:
        if abs(r2 - r1) < abs(c2 - c1):
            king = abs(r2 - r1) + abs(c2 - c1 + abs(r2 - r1 ))
        else:
            king = abs(c2 - c1) + abs(r2 - r1 + abs(c2 - c1))
         
    print(rook, bishop, king)

if __name__ == '__main__':
    main()