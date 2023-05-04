    def main():
        n, t = map(int, input().split())
        studs = list(input())
        
        for _ in range(t):
            indx = 0
            while indx < n - 1:
                if studs[indx] == 'B' and studs[indx + 1] == 'G':
                    studs[indx], studs[indx + 1] = studs[indx + 1], studs[indx]
                    indx += 1
                indx += 1
        
        print(''.join(studs))

    if __name__ == '__main__':
        main()

