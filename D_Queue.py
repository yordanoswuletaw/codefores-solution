def main():
    childrens = list(input())
    n = len(childrens)
    ans = 0
    hasF = False
    holder = n - 1
    prev = 0
    while holder >= 0:
        if childrens[holder] == 'F':
            hasF = True
        if childrens[holder] == 'M':
            if hasF:
                ans += 1
            holder -= 1
            continue

        seeker = holder 
        while seeker >= 0 and childrens[seeker] == 'F':
            seeker -= 1
        if seeker < 0:
            break
        curr = holder - seeker - 1
        if curr > prev:
            ans += curr - prev
            prev = curr
        holder = seeker
    
    print(ans)

if __name__ == '__main__':
    main()