arrLen = int(input())
array = list(map(int, input().split()))

queryLen = int(input())
queries = list(map(int, input().split()))

output = [0,0]
hashMap = {}
for i in range(arrLen):
    hashMap[array[i]] = i 

for query in queries:

    indx = hashMap.get(query, -1)
    if indx == -1:
        output[0] += arrLen
        output[1] += arrLen
    else:
        output[0] += indx + 1
        output[1] += arrLen - indx 

print(output[0], output[1])
