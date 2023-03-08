



for _ in range(int(input())):
    n = int(input())
    digits = list(map(int, input()))
    prfxSum = [0]
    for digit in digits:
        prfxSum.append(prfxSum[-1] + digit)
    
    left, right = 0, 1
    output = 0
    while right < n:
        
        output += int((right - left) == (prfxSum[right] - prfxSum[left]))

        if (right - left) < (prfxSum[right] - prfxSum[left]) or (right - left) <= 1:
            right += 1
        else:
            left += 1

       

    print(output)


