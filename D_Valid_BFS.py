from collections import defaultdict, deque

def main():
    n = int(input())
    tree = defaultdict(list)
    for _ in range(n - 1):
        v1, v2 = map(int, input().split())
        tree[v1].append(v2)
        tree[v2].append(v1)
    
    seq = list(map(int, input().split()))
    seqbfs = {v:indx for indx, v in enumerate(seq)}

    if seq[0] != 1:
        print('No')
    else:
        queue = deque([1])
        visited = set([1])
        indx = 1

        while queue:
            v = queue.popleft()
            for neib in sorted(tree[v], key=lambda each: seqbfs[each]):
                if neib not in visited:
                    if neib == seq[indx]:
                        indx += 1
                    queue.append(neib)
                    visited.add(neib)
        if indx >= len(seq):
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
