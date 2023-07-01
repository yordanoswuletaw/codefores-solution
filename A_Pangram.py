def main():
    n = int(input())
    sentence = input().lower()
    freq = [0] * 26
    for char in sentence:
        freq[ord(char) % 97] += 1
   
    ans = 'YES'
    for each in freq:
        if each == 0:
            ans = 'NO'
            break
    print(ans)

if __name__ == '__main__':
    main()