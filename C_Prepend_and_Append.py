for _ in range(int(input())):
    
    n = int(input())
    string = input()
    if n == 1:
        print(1)
    else:
        i, j = 0, n - 1
        while i <= j and string[i] != string[j]:
            i += 1
            j -= 1
        print(len(string[i:j+1]))