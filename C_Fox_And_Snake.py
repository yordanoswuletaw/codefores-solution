import sys, threading

input = lambda: sys.stdin.readline().strip()


def main():
    n, m = map(int, input().split())

    grid = []
    right = True
    for i in range(n):
        if i % 2 == 0:
            grid.append('#' * m)
        else:
            if right:
                grid.append(('.' * (m - 1)) + '#')
            else:
                 grid.append('#' + ('.' * (m - 1)))
            right = not right 
    
    for each in grid:
        print(each)
    


if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
 
