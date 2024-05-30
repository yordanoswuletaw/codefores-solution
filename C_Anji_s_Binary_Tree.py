from collections import defaultdict

def main():
    for _ in range(int(input())):
        n = int(input())
        ltrs = input()
        graph = defaultdict(list)
        visited = set()
        for v in range(n):
            l, r = map(int, input().split())
            graph[v].append(max(0, l - 1))
            graph[v].append(max(0, r - 1))

        stack = [(0, 0)]
        ans = float('inf')
        while stack:
            v, res = stack.pop()
            if v in visited:
                continue
            visited.add(v)
            left = graph[v][0]
            right = graph[v][1]
            if not left and not right:
                ans = min(ans, res)
            if left:
                stack.append((left, res + int(ltrs[v] != 'L')))
            if right:
                stack.append((right, res + int(ltrs[v] != 'R')))

        print(ans)
    
    
if __name__ == '__main__':
    main()