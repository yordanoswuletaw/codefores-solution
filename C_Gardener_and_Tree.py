from collections import defaultdict, deque

def main():
    for _ in range(int(input())):
        input()
        n, k = map(int, input().split())
        graph = defaultdict(list)
        degree = defaultdict(int)

        for _ in range(n - 1):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        queue = deque()
        for key, val in degree.items():
            if val == 1:
                 queue.append((key, 1))
        
        ans = 0
        while queue:
            node, h = queue.popleft()
            if h > k:
                ans += 1
            for nxt in graph[node]:
                degree[nxt] -= 1
                if degree[nxt] == 1:
                    queue.append((nxt, h + 1))
        
        print(ans)

if __name__ == '__main__':
    main()