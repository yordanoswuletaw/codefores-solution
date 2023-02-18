n = int(input())

events = []
for _ in range(n):
    events.append(tuple(map(int, input().split())))
res = 0
events.sort(key=lambda e: (e[0], -e[1]))

i, j = 0, 1
eventsIncluded = 0
while j < n:
    if events[i][0] < events[j][0] and events[i][1] > events[j][1]:
        eventsIncluded += 1
        j += 1
    else:
        i = j 
        j += 1

print(eventsIncluded) 