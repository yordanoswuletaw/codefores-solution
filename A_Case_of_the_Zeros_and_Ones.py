def main():
    n = int(input())
    strings = input()

    stack = []
    for char in strings:
        if stack and stack[-1] != char:
            stack.pop()
        else:
            stack.append(char)
    
    print(len(stack))

if __name__ == '__main__':
    main()