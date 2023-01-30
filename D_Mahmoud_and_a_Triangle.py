



def check(sides, n):
    i, j, k = 0, 1, 2
    while k < n:
        if sides[i] < sides[j] + sides[k] and sides[j] < sides[i] + sides[j] and sides[k] < sides[i] + sides[j]:
            return 'YES'
        i += 1
        j += 1
        k += 1
    return 'NO'

n = int(input())
sides = list(map(int, input().split()))
print(check(sorted(sides), n))