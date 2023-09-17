def main():
    str1 = input()
    str2 = input() 

    if len(str1) != len(str2):
        if len(str1) <= len(str2):
            print(len(str2))
        else:
            print(len(str1))
        exit()

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            print(len(str1))
            exit()
    
    print(-1)

if __name__ == '__main__':
    main()