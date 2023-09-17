def main():
    num = input()

    digits = 0
    for digit in num:
        if digit == '7' or digit == '4':
            digits += 1

    if digits == 7 or digits == 4:
        print('YES')
    else:
        print('NO') 

if __name__ == '__main__':
    main()