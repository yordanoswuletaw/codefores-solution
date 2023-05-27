from collections import defaultdict, deque

def bfs(n, d, jumps):
    moves = 0
    queue = deque([(0, 0)])
    visited = set([0])

    while queue:
        for _ in range(len(queue)):
            v, jmps = queue.popleft()
            #print(jmps)
            if jmps >= n - 1:
                return moves
            for i in range(1, d + 1):
                indx = v + i
                if indx not in visited and indx < len(jumps) and jumps[indx]:
                    queue.append((indx, jmps + i))
                    visited.add(indx)
        moves += 1
    
    return -1

def main():
    n, d = map(int, input().split()) 
    jumps = list(map(int, input()))
    print(bfs(n, d, jumps))

if __name__ == '__main__':
    main()