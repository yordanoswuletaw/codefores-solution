






def checkOverFlow():
    stack, res = [], 0
    for _ in range(int(input())):
        cmds = input()
        if cmds == 'add':
            if stack and stack[-1] + res <= (2 ** 32 - 1):
                res += stack[-1]
            elif not stack and res + 1 <= (2 ** 32 - 1):
                res += 1
            else:
                return 'OVERFLOW!!!'
            
        elif cmds == 'end':
            if stack:
                stack.pop() 
                
        else:
            num = int(cmds.split()[1])
            if stack and stack[-1] * num <=  (2 ** 32 - 1):
                stack.append(stack[-1] * num)
            elif not stack:
                stack.append(num)
            else:
                  stack.append(2 ** 32)
    return res

print(checkOverFlow())

