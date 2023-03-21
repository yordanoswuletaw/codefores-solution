





brackets = input()
stack = []
res = 0
for each in brackets:
    if stack and each == ')':
        stack.pop()
        res += 2
    elif each == '(':
        stack.append(each)

print(res)