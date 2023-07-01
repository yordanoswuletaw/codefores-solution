from collections import defaultdict, deque

def main():
    n, m, k = map(int, input().split())
    graph = defaultdict(list)
    weight = defaultdict(lambda: float('inf'))

    for _ in range(m):
        u, v, l = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        weight[(u, v)] = min(weight[(u, v)], l)
        weight[(v, u)] = min(weight[(v, u)], l)
    
    storage = []
    if k > 0:
        storage = list(map(int, input().split()))
    
    queue = deque()
    visited = set()
    for each in storage:
        queue.append((each, 0))
        visited.add(each)

    ans = float('inf')
    storage = set(storage)
    while queue:
        node, l = queue.popleft()
        if node not in storage:
            ans = min(ans, l)
            
        visited.add(node)
        if l == 0:
            for nxt in graph[node]:
                if nxt in visited:
                    continue
                queue.append((nxt, weight[(node, nxt)] + l))
    
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()