





n = int(input())
ops = []
for _ in range(n):
    op = input()
    if op == 'add' or op == 'end':
        ops.append(op)
    else:
        ops.append(int(op.split(' ')[1]))

def catchOverflow():
    stack = []
    x = 0
    cp = 0
    for op in ops:
        if op == 'add':
            if stack:
                if x + stack[-1] > (2 ** 32 - 1):
                     return 'OVERFLOW!!!'
                x += stack[-1]
                continue
            if x + 1 > ( 2 ** 32 - 1):
                return 'OVERFLOW!!!'
            x += 1
        elif op == 'end':
            if cp > 0:
                cp -= 1
                continue
            if stack:
                stack.pop()
        else:
            if stack:
                if stack[-1] >= (2 ** 32 - 1):
                    cp += 1
                    continue
                stack.append(stack[-1] * op)
            else:
                stack.append(op)
    return x

print(catchOverflow())
