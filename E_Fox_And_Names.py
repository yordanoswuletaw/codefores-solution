from collections import defaultdict, deque

def main():
    n = int(input())
    names = []
    for _ in range(n):
        names.append(input())

    graph, indegree = defaultdict(list), defaultdict(int)

    for i in range(1, n):
        prev, nxt = names[i - 1], names[i]
        l1, l2 = len(prev), len(nxt)
        for j in range(min(l1, l2)):
            if prev[j] != nxt[j]:
                if prev[j] > nxt[j]:
                    graph[prev[j]].append(nxt[j])
                    indegree[nxt[j]] += 1
                    indegree[prev[j]] += 0
                break
    
    queue = deque()
    order = []
    for key, val in indegree.items():
        if val ==  0:
            queue.append(key)
    while queue:
        char = queue.popleft()
        order.append(char)
        for nxt in graph[char]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    
    print(order)
    
    # if len(order) < 26:
    #     print("Impossible")
    # else:
    #     print(''.join(order))

if __name__ == '__main__':
    main()