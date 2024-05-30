def main():
    for _ in range(int(input())):
        n = int(input())
        ribbon = list(map(int, input().split()))

        left = ribbon.index(1)
        right = left
        for i in range(n - 1, left, - 1):
            if ribbon[i] == 1:
                right = i 
                break
        print(ribbon[left : right].count(0))

if __name__ == '__main__':
    main() 