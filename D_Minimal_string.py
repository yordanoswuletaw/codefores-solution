







string = input()

t, u = [], []
hashSet = [0] * 26
for s in string:
    hashSet[ord(s) - 97] += 1

for i in range(len(string)):
    t.append(string[i])
    hashSet[ord(string[i]) - 97] -= 1
    while t and hashSet[:ord(t[-1]) - 97].count(0) == ord(t[-1]) - 97:
        u.append(t.pop())


print(''.join(u))

