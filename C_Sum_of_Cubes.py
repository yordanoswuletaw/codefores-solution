def checkSum(num):

    left, right = 1, int(pow(num, 1/3))

    while left <= right:
        res = left ** 3 + right ** 3
        if res == num:
            return 'YES'
        elif res > num:
            right -= 1
        else:
            left += 1
    return 'NO'


for _ in range(int(input())):
    print(checkSum(int(input())))