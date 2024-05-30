def main():
    for _ in range(int(input())):
        n = int(input())
        scores = sorted(zip(map(int, input().split()), map(int, input().split())), key=lambda x: x[1] + x[0], reverse=True)
        score = sum([x[0] - 1 for x in scores[::2]]) - sum([x[1] - 1 for x in scores[1::2]])
        print(score)

if __name__ == '__main__':
    main()