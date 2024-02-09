from collections import defaultdict, deque
def fndRoads(railways, n):
    roads = defaultdict(list)
    for i in range(1, n):
        for j in range(n, i, -1):
            if j not in railways[i]:
                roads[i].append(j)
    
    return roads

def findTimeTaken(graph, n):
    queue = deque([(1, 0)])
    visited = set([1])
    while queue:
        node, dist = queue.popleft()
        if node == n:
            return dist
        for nb in graph[node]:
            if nb not in visited:
                queue.append((nb, dist + 1))
                visited.add(nb)
    
    return -1
    
def main():
    n, m = map(int, input().split())
    railways = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        railways[u].append(v)
        railways[v].append(u)
    
    roads = fndRoads(railways, n)
    print(roads)
    t1 = findTimeTaken(railways, n)
    t2 = findTimeTaken(roads, n)
    if t1 == -1 or t2 == -1:
        print(-1, t1, t2)
    else:
        print(max(t1, t2))
    
if __name__ == '__main__':
    main()