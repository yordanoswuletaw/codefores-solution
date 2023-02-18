pi = '314159265358979323846264338327'
n = int(input())
for _ in range(n):
    digits = input()
    digitsCount = 0
    for i in range(len(digits)):
        if digits[i] != pi[i]:
            break
        digitsCount += 1
    print(digitsCount)