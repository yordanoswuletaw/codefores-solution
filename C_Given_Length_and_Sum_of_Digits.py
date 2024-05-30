d, s = map(int, input().split())
if d == 1 and s == 0:
    print(0, 0)
elif s == 0 or d < len(str(s)):
    print(-1, -1)
else:
    ans = [9] * d
    for i in range(d):
        if s == sum(ans):
            break
        for j in range(9):
            if i == 0 and j == 0:
                continue
            ans[i] = j 
            if sum(ans) >= s:
                break 

    max_val = [9] * d 
    for i in range(d-1, -1, -1):
        if s == sum(max_val):
            break
        for j in range(9, -1, -1):
            max_val[i] = j 
            if sum(max_val) <= s:
                break 
    if sum(ans) != s or sum(max_val) != s:
        print(-1, -1)
    else:
        print(''.join([str(e) for e in ans]), ''.join([str(e) for e in max_val]))
