



n = int(input())
cost = list(map(int, input().split()))

normalSum = [0]
sortedSum = [0]
for num in cost:
    normalSum.append(normalSum[-1] + num)

for num in sorted(cost):
    sortedSum.append(sortedSum[-1] + num)

m = int(input())
queries = []
for _ in range(m):
    queries.append(list(map(int, input().split())))

output = []
for query in queries:
    if query[0] == 1:
        output.append(normalSum[query[2]] - normalSum[query[1]-1]) 
    else:
        output.append(sortedSum[query[2]] - sortedSum[query[1]-1]) 
for each in output:
   print(each)

