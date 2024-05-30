def main():
    inp = list(input())
    t, u = [], []
    chars = [0] * 26
    for char in inp:
        num = ord(char) - 97
        chars[num] += 1
    # print(chars)
    def check(char):
        num = ord(char) - 97
        return sum(chars[:num]) <= 0

    for char in inp:
        t.append(char)
        num = ord(char) - 97
        chars[num] -= 1
        while t and check(t[-1]):
            num = ord(t[-1]) - 97
            u.append(t.pop())
    while t:
        top = t.pop()
        num =  ord(top) - 97
        chars[num] -= 1
        u.append(top)

    print(''.join(u))

if __name__ == '__main__':
    main()