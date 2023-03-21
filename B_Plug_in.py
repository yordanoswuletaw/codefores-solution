




words = input()

duplicate = set()
stack = []

for i, char in enumerate(words):
    if stack and stack[-1] == char:
        stack.pop()
    else:
        stack.append(char)

print("".join(stack))