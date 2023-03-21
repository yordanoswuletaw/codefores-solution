


from collections import defaultdict

from math import factorial, pow
from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    digits = list(map(int, input()))
    prfxSum = [0]
    subComb = defaultdict(int)
    for digit in digits:
        prfxSum.append(prfxSum[-1] + digit)
    
    for i, each in enumerate(prfxSum):
        subComb[each - i] += 1
    
    res = 0
    for val in subComb.values():
        if val > 1:
            res += factorial(val) // (factorial(val - 2) * factorial(2))
    
    print(res)
pow()