import sys, threading

input = lambda: sys.stdin.readline().strip()


def main():
    a, b = map(int, input().split())

    ans = 'NO'
    sequence = []

    def dfs(a, b, seq):
        nonlocal ans
        nonlocal sequence
        if a == b:
            ans = 'YES'
            sequence = seq[:]
            sequence.append(a)
            return
        if a > b:
            return 
        seq1 = seq.copy()
        seq1.append(a)
        seq2 = seq.copy()
        seq2.append(a)
        dfs(a * 2, b, seq1)
        dfs(a * 10 + 1, b, seq2)
    
    dfs(a, b, [])
    print(ans)
    if ans == 'YES':
        print(len(sequence))
        print(*sequence)

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
 
