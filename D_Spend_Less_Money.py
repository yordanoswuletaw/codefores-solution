


n, k = map(int, input().split())
right = list(map(int, input().split()))
after = list(map(int, input().split()))

hashMap = []

for i in range(n):
    hashMap.append([right[i], after[i]])

hashMap.sort(key=lambda x: x[0], reverse=True)

'''
10 7 4 3 3
12 5 5 5 6
'''

res = 0
i = j = 0
l = 0
indxs = set()
while j < n:
    if l >= k:
        break
    while j < n and hashMap[i][1] == hashMap[j][1]:
        j += 1
    if i < n and j < n  and hashMap[i][0] >= hashMap[j][0]:
        res += hashMap[j-1][0]
        l += 1
        indxs.add(j-1)
    i = j

for i in range(n):
    if i not in indxs:
        # if l < k:
        #     res += hashMap[i][0]
        #     l += 1
        # else:
        res += min(hashMap[i][0], hashMap[i][1])
print(res)
