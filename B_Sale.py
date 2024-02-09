n, m = map(int, input().split())
tvSets = list(map(int, input().split()))    
tvSets.sort()
ans = 0
for i in range(m):
    if tvSets[i] < 0:
        ans += tvSets[i]
    else:
        break
print(-ans)