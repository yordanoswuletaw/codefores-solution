











for _ in range(int(input())):
    w, t, f = map(int, input().split())
    option1 = f * w + (4 -  f) * t 
    option2 = t * (4  + f)
    option3 = 4 * w
    print(min(option1, option2, option3))