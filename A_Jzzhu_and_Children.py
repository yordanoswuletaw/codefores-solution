from collections import deque

n, m = map(int, input().split())
children = deque(map(int, input().split()))

queue = deque(range(1, n + 1))

while len(queue) > 1:
    currVal = children.popleft()
    currChild = queue.popleft()
    if currVal - m > 0:
        children.append(currVal - m)
        queue.append(currChild) 

print(queue.pop())