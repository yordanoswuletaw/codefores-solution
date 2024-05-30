from collections import defaultdict

def main():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    init = list(map(int, input().split()))  
    goal = list(map(int, input().split()))

    ops = 0
    nodes = []
    stack = [(1, init[0] != goal[0], False, 0)]
    if stack[0][1]:
        ops += 1
        nodes.append(1)
    visited = set()
    while stack:
        node, even, odd, level = stack.pop()
        visited.add(node)
        level += 1
        for neib in graph[node]:
            if neib not in visited:
                if level % 2:
                    nxt_odd = odd
                    if nxt_odd:
                        if init[neib - 1] == goal[neib - 1]:
                            nodes.append(neib)
                            ops += 1
                            nxt_odd = not nxt_odd
                    else:
                        if init[neib - 1] != goal[neib - 1]:
                            nodes.append(neib)
                            ops += 1
                            nxt_odd = not nxt_odd
                    stack.append((neib, even, nxt_odd, level))
                else:
                    nxt_even = even
                    if nxt_even:
                        if init[neib - 1] == goal[neib - 1]:
                            nodes.append(neib)
                            ops += 1
                            nxt_even = not nxt_even 
                    else:
                        if init[neib - 1] != goal[neib - 1]:
                            nodes.append(neib)
                            ops += 1
                            nxt_even = not nxt_even
                    stack.append((neib, nxt_even, odd, level))

    print(ops)
    for node in nodes:
        print(node)

    
if __name__ == '__main__':
    main()
 
 