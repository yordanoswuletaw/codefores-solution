def invertZeros(binary, inversions, zeros):
    ones = 0
    result = inversions
    for each in binary:
        if each:
            ones += 1
        else:
            zeros -= 1
            result = max(result, inversions + zeros - ones)
    return result
        

def invertOnes(binary, inversions, ones):
    zeros = 0
    result = inversions
    for each in binary[::-1]:
        if each:
            ones -= 1
            result = max(result, inversions + ones - zeros)
        else:
            zeros += 1
    return result 

for _ in range(int(input())):
    binaryLen = int(input())
    binary = list(map(int, input().split()))

    inversions = 0
    ones, zeros = 0, 0

    for each in binary:
        if each:
            ones += 1
        else:
            inversions += ones
            zeros += 1
    
    print(max(inversions, invertZeros(binary, inversions, zeros), invertOnes(binary, inversions, ones)))

