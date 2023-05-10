from math import log 

def main():
    for _ in range(int(input())):
        n = int(input())
        x = log(n, 2)
        if x == int(x):
            print('NO')
        else:
            print('YES')


if __name__ == '__main__':
    main()

