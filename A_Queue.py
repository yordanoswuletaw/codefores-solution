





n = int(input())
times = sorted(map(int, input().split()))
res = 0
indx= 0
prfxSum = 0
while indx < n:
    if prfxSum <= times[indx]:
        prfxSum += times[indx]
        res += 1
    indx += 1
print(res)