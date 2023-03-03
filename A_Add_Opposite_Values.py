for _ in range(int(input())):
    

    n = int(input())
    strings = input()
    l, r = 0, n - 1
    while l <= r and strings[l] != strings[r]:
        l += 1
        r -= 1
    print(r - l + 1)