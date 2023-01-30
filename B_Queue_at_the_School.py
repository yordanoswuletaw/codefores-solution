n, t = map(int, input().split())
queue = list(input())

while t > 0:
    indx = 0 
    while indx < len(queue) - 1:
        if queue[indx] == 'B' and queue[indx + 1] == 'G':
            queue[indx], queue[indx + 1] = queue[indx + 1], queue[indx]
            indx += 1
        indx += 1
    t -= 1

print(''.join(queue))