n = int(input())
points = []

for _ in range(n):
    points.append(tuple(map(int, input().split())))

res = 0
for pi in points:
    left = right = upper = lower = False
    for pj in points:
        if pi[0] == pj[0]:
            if pi[1] > pj[1]:
                lower = True 
            elif pi[1] < pj[1]:
                upper = True 
        if pi[1] == pj[1]:
            if pi[0] > pj[0]:
                left = True 
            elif pi[0] < pj[0]:
                right = True 
    if left and right and upper and lower:
        res += 1

print(res)