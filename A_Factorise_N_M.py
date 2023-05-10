def main():
    for _ in range(int(input())):
        n = int(input())

        if n == 2:
            print(7)
        else:
           for i in (3, 5, 7, 9):
               if i != n:
                   print(i)
                   break


if __name__ == '__main__':
    main()

