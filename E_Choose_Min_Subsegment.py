




n = int(input())
a = list(map(int, input().split()))

size, prefix = n, set()

for i in range(n):

    if len(prefix) < i: break 
    
    suffix = set()
    for j in range(n - 1, i - 2, -1):
        if j < i or a[j] in prefix or a[j] in suffix:
            break 
        suffix.add(a[j])
    
    size = min(size, j - i + 1) 

    prefix.add(a[i])

print(size)