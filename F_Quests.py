for _ in range(int(input())):
    n, c, d = map(int, input().split())
    rewards = list(map(int, input().split()))

    rewards.sort(reverse=True)
    if rewards[0] > c:
        print('Infinity')
    elif rewards[0] * d < c:
        print('Impossible')
    else:
        trial = rewards[0] * 2 
        
