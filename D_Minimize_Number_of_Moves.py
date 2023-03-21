









def compute(string, char, n):
    if n == 0:
        return 0
    if n == 1:
        if ord(string[0]) != ord(char) + 1:
            return 1
        return 0
    if n == 2:
        cnt = 0
        if ord(string[0]) != ord(char) + 1:
            cnt += 1
        if ord(string[1]) != ord(char):
            cnt += 1
        return cnt 
    lftCnt, rghtCnt = string[:n//2].count(char), string[n//2:].count(char)
    if lftCnt >= rghtCnt:
        return n // 2 - lftCnt + compute(string[n//2:], chr(ord(char) + 1), n//2)
    else:
        return n // 2 - rghtCnt + compute(string[:n//2], chr(ord(char) + 1), n //2)



for _ in range(int(input())):
    n = int(input())
    string = input()
    leftCount, rightCount = string[:n//2].count('a'), string[n//2:].count('a')
    res = 0
    if leftCount >= rightCount:
        res += n // 2 - leftCount + compute(string[n//2:], 'b', n//2)
    else:
         res += n // 2 - rightCount + compute(string[:n//2], 'b', n //2)
    print(res)
