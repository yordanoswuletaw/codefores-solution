word = input()
diff = 0

for char in word:
    if char.isupper():
        diff += 1
    else:
        diff -= 1

if diff <= 0:
    print(word.lower())
else:
    print(word.upper())
