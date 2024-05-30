from collections import deque, defaultdict

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    odds = [(i + 1, 0) for i, num in enumerate(nums) if num % 2]
    evens = [(i + 1, 0) for i, num in enumerate(nums) if num % 2 == 0]
    graph = defaultdict(list)

    for i, num in enumerate(nums):
        indx = i + 1
        left, right = indx + num, indx - num
        if 1 <= left <= n:
            graph[left].append(indx)
        if 1 <= right <= n:
            graph[right].append(indx)

    ans = [float('inf')] * n 
    def bfs(source, target):
        queue = deque(source)
        visited = set()
        while queue:
            for _ in range(len(queue)):
                indx, moves = queue.popleft()
                num = nums[indx - 1]
                if target and num % 2:
                    ans[indx - 1] = min(ans[indx - 1], moves)
                if not target and num % 2 == 0:
                    ans[indx - 1] = min(ans[indx - 1], moves)
                if indx in visited:
                    continue
                visited.add(indx)
                for neib in graph[indx]:
                    queue.append((neib, moves + 1))
    
    bfs(odds, False)
    bfs(evens, True)
    print(*[-1 if num == float('inf') else num for num in ans])
    
if __name__ == '__main__':
    main()
 
 