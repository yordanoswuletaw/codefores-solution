def main():
    num1 = input()
    num2 = input()

    n = len(max(num1, num2))
    ans = []

    for i in range(n ):
       ans.append(str(int(num1[i]) ^ int(num2[i])))

    print(''.join(ans))
    

if __name__ == '__main__':
    main()

