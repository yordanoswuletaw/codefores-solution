def main():
    ltr = list(input())
    caps = smls = 0  

    for end in range(len(ltr)):
        caps += int(ltr[end].isupper())
        smls += int(ltr[end].islower())

    for i in range(len(ltr)):
        if ltr[i].islower():
            break
        caps -= 1
    
    for i in range(len(ltr) - 1, - 1, -1):
        if ltr[i].isupper():
            break
        smls -= 1
       
    print(min(caps, smls))
        


if __name__ == '__main__':
    main()