from collections import defaultdict, deque

def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        graph = defaultdict(list)
        in_degree = [0] * n 
        out_degree = [0] * n

        for _ in range(m):
            typ, u, v = map(int, input().split())
            u, v = u - 1, v - 1
            if typ:
                graph[u].append((v, 1))
                in_degree[v] += 1
                out_degree[u] += 1
            else:
                graph[u].append((v, 0))
                graph[v].append((u, 0))
                
        order = set()
        queue = deque()
        for node in range(n):
            if in_degree[node] == 0 and out_degree[node] == 0:
                queue.append(node) 
        
        for node in range(n):
            if in_degree[node] == 0 and out_degree[node] != 0:
                queue.append(node) 
        
        while queue:
            node = queue.popleft()
            for neighbor, typ in graph[node]:
                if typ:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
                    order.add((node + 1, neighbor + 1))
                else:
                    if (neighbor + 1, node + 1) not in order:
                        order.add((node + 1, neighbor + 1))
                        
        
        if sum(in_degree) != 0:
            print('NO')
            continue
        
        print('YES')
        for u, v in order:
            print(u, v)

    
if __name__ == '__main__':
    main()
 