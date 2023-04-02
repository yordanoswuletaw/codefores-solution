





n = int(input())
ops = list(input())

stack = 0 
stones = 0

for op in ops:
    if op == '+':
        stack += 1
    else:
        stack -= 1
    if stack < 0:
        stones += 1
        stack += 1

print(stones + ops.count('+') - ops.count('-'))