def main():
    stack = ['']
    for _ in range(int(input())):
        cmd =  list(input().split())
        if cmd[0] == 'cd':
            cmds = cmd[1].split('/')
            if cmds[0] == '': stack = ['']
            for c in cmds:
                if c == '..':
                    stack.pop()
                elif c != '':
                    stack.append(c.strip())
        else:
            print('/'.join(stack) + '/')

if __name__ == '__main__':
    main()