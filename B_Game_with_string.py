def main():
    string = input()
    stack = []
    turns = 0
    for char in string:
        if stack and stack[-1] == char:
            stack.pop()
            turns += 1
        else:
            stack.append(char)
    
    print("Yes" if turns % 2 else "No")

if __name__ == '__main__':
    main()