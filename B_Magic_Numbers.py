import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    numbers = [1, 14, 144]
    num = int(input())
    ans = 'NO'

    def dfs(currNum, num):
        nonlocal ans
        if currNum == num:
            ans = 'YES'
            return
        if currNum > num:
            return
        
        for each in numbers:
            l = len(str(each))
            digit = int('1' + ('0' * l))
            dfs(currNum * digit + each, num)
    
    dfs(0, num)
    print(ans)


if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
 
