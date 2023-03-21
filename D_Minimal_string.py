







string = input()

t, u = [], []

for i, char in enumerate(string):
    if not t or t[-1] > char:
        if not u or u[-1] < char:
            t.append(char)
        else:
            u.append(char)
    elif t and t[-1] < char:
         while not u or t and ord(t[-1]) - ord(char) < ord(u[-1]) - ord(char):
            u.append(t.pop())
         t.append(char)

if t:
    if t[0] > t[-1]:
        t = t[::-1]
if u:
    if u[0] > u[-1]:
        u = u[::-1]

print(''.join(u + t))
