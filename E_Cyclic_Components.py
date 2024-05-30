from collections import defaultdict

def main():
    V, E = list(map(int, input().split()))
    graph = defaultdict(list)

    # represent the graph with an adjacency list
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    cyclic_connected_components = 0
    visited = set()

    # count the number of cyclic connected components
    for node in graph:
        if node not in visited:
            stack = [node]
        
            while stack:
                current = stack.pop()
                # if the current node has more than 2 neighbors, it is not a cyclic connected component
                if len(graph[current]) != 2:
                    cyclic_connected_components -= 1
                    break

                visited.add(current)
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)

            cyclic_connected_components += 1
    
    print(cyclic_connected_components)
    
if __name__ == '__main__':
    main()
