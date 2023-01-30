n = int(input())
letters = {}
for indx, char in enumerate('abcdefghijklmnopqrstuvwxyz'):
    letters[char] = indx + 1

for _ in range(n):
    wordLen = int(input())
    word = input()
    minSize = 0
    for char in word:
        minSize = max(minSize, letters[char])
    print(minSize)