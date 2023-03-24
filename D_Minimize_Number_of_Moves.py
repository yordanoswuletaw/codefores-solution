









def compute(string, char, n):
    if n == 1:
        if char == string[0]:
            return 0
        return 1
    lHalf = string[:n//2]
    lCount = lHalf.count(char)

    rHalf = string[n//2:]
    rCount = rHalf.count(char)

    return min(n//2 - lCount + compute(rHalf, chr(ord(char) + 1), n//2 ), n//2 - rCount + compute(lHalf, chr(ord(char) + 1), n//2))
    

for _ in range(int(input())):
    n = int(input())
    string = input()
    print(compute(string, 'a', n))
