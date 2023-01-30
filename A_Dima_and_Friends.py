players = int(input()) + 1
fingers = sum(map(int, input().split()))


for i in range(1, 6):
    if (i + fingers) % players != 1:
        print(i)
        break

# res = players - (fingers % players)
# print(res)

