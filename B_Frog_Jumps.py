def main():
    for _ in range(int(input())):
        jumps = list(input())

        res = 1 
        i = 0
        while i < len(jumps):
            if jumps[i] == 'L':
                j = i + 1
                while j < len(jumps) and jumps[j] == 'L':
                    j += 1
                res = max(res, j - i + 1)
                i = max(i, j)
            else:
                i += 1

        print(res) 

if __name__ == '__main__':
    main()