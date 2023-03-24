





    















n, l, r = map(int, input().split())

# geting range of the actural number
def getRange(n):
    rng = pw = 0
    while n:
        rng += 2 ** pw 
        pw += 1
        n //= 2
    return rng

# checking range bound
def outOfRange(start, end, l, r):
    return r < start or l > end

# compute ones in the given range
def compute(n, start, end, l, r):
    if outOfRange(start, end, l, r) :
        return 0 
    if n == 0 or n == 1:
        return n 
     
    rng = (start + end) // 2
    return compute(n//2, start, rng - 1, l, r) + compute(n % 2, rng, rng, l, r) + compute(n//2, rng + 1, end, l, r)

print(compute(n, 1, getRange(n), l, r))







