


n, m, k = map(int, input().split())

array = list(map(int, input().split()))

ops = []
for _ in range(m):
    ops.append(list(map(int, input().split())))

queries = []
for _ in range(k):
     queries.append(list(map(int, input().split())))

# prefix sum of queries that applied in the operation
querySum = [0] * (m + 1)
for query in queries:
     querySum[query[0]-1] += 1
     querySum[query[1]] -= 1

for i in range(1, m + 1):
     querySum[i] += querySum[i-1]   

# prefix sum of operations that directly applied to the array
opsSum = [0] * (n + 1)
for i,op in enumerate(ops):
     opsSum[op[0]-1] += op[2] * querySum[i]
     opsSum[op[1]] -= op[2] * querySum[i]

for i in range(1, n + 1):
     opsSum[i] += opsSum[i-1]   

for i in range(n):
     array[i] += opsSum[i]

print(*array)