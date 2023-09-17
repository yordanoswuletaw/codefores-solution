def main():
    string = input()

    stack = []

    for char in string:
        while stack and stack[-1] < char:
            stack.pop()
        stack.append(char)

    print(''.join(stack)) 

if __name__ == '__main__':
    main()