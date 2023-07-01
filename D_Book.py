from collections import defaultdict, deque

def main():
    for _ in range(int(input())):
        n = int(input())
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(n):
            chapters = list(map(int, input().split()))
            for each in chapters[1:]:
                graph[each - 1].append(i)
                indegree[i] += 1
        print(indegree)


if __name__ == '__main__':
    main()