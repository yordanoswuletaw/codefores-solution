


from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    digits = list(map(int, input()))
    prfxSum = [0]
    for digit in digits:
        prfxSum.append(prfxSum[-1] + digit)
    

    diff = {}
    for i in range(n + 1):
        if prfxSum[i] - i in diff:
            diff[prfxSum[i] - i] = diff[prfxSum[i] - i] * 2 + 1 
        else:
            diff[prfxSum[i] - i] = 0

    # output = 0
    # print(diff)
    # for key, value in diff.items():
    #     if value > 1:
    #         output += value
    print(sum(diff.values()))
