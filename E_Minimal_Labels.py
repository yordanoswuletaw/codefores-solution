from collections import deque, defaultdict

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    count = [0] * n

    for _ in range(m):
        v, u = map(int, input().split()) 
        graph[v].append(u)
        count[u - 1] += 1
    
    print(count)
    queue = deque()
    for i in range(n):
        if count[i] == 0:
            queue.append(i + 1)
    
    ans = [0] * n 
    # while queue:
    #     node = queue.popleft()
    #     ans[node ]
    #     for neib in graph[node]:


if __name__ == '__main__':
    main()