from math import lcm
def main():
    for _ in range(int(input())):
        n = int(input())
        strings = list(input())
        perms = list(map(int, input().split()))

        graph = {}
        for i in range(n):
            graph[i] = perms[i] - 1
        
        colors = [-1] * n  
        ops = []
        def dfs(node, depth):
            if colors[node] == 0:
                count = 0
                for i in range(0, len(depth)):
                    cpy_dpt = depth[i+1:] + depth[:i+1]
                    count += 1
                    if cpy_dpt == depth:
                        break
                ops.append(count)
                return True 
            
            if colors[node] == 1:
                return False
            
            colors[node] = 0
            nxt = graph[node]
            depth.append(strings[nxt])
            if dfs(nxt, depth):
                colors[node] = 1
                return True

        for node in range(n):
            if colors[node] == -1:
                dfs(node, [])

        print(lcm(*ops))

if __name__ == '__main__':
    main()  