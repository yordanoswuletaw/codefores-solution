def main():
    w, h = map(int, input().split())

    if w == 1:
        print(h // 2)
    elif h == 1:
        print( w // 2)
    else:
        ans = 0
        if w > h:
            ans = w * (h // 2)
            h %= 2
            ans += h * w // 2
        else:
            ans = h * (w // 2)
            w %= 2
            ans += w * h // 2
        print(ans)

if __name__ == '__main__':
    main()