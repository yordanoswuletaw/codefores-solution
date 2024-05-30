def main():
    brackets = list(input())
    stack = []
    opend = 0
    longest = count = 0

    for bracket in brackets:
        if bracket == ')':
            opend -= 1
            if opend < 0:
                while stack:
                    currAns = 0
                    while stack and stack[-1] != '(': 
                        currAns += stack.pop()
                    longest = max(longest, currAns)
                    if currAns:
                        count += 1
                    if stack:
                        stack.pop()
                opend = 0
            else:
                currAns = 0
                while stack and stack[-1] != '(':
                    currAns += stack.pop()
                if stack:
                    stack.pop()
                    currAns += 2
                stack.append(currAns) 
        else:
            opend += 1 
            stack.append(bracket)
    #print(stack, count)
    while stack:
        currAns = 0
        while stack and stack[-1] != '(': 
            currAns += stack.pop()
        longest = max(longest, currAns)
        if currAns:
            count += 1
        if stack:
            stack.pop()
       
    if not longest:
        count = 1
    print(longest, count)
    

if __name__ == '__main__':
    main()