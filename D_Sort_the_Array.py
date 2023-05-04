def main():
    n = int(input())

    nums = list(map(int, input().split()))

    dec = []
    inc = []

    for num in nums:
        while dec and dec[-1] < num:
            dec.pop()
        while inc and inc[-1] > num:
            inc.pop()
        dec.append(num)
        inc.append(num)
    
    if len(inc) > 1 and dec:
        if dec[0] > inc[0]:
            print('no')
        else:
            print('yes')
            print(*dec)
    else:
        print('yes')
        print(inc)


    


if __name__ == '__main__':
    main()

