





words = input()

def checkWord(words):

    hashMap = [0] * 26
    count = ptr = 0

    for i,char in enumerate(words):
        if char != '?' and hashMap[ord(char) % 65] != 0:
            print("gettingherere")
            ptr = i 
            hashMap = [0] * 26
            count = 0
        if len(words) -  ptr < 26:
            return -1
        if count + len(hashMap) == 26:
            output = [0] * 26
            for i in range(26):
                if hashMap[i] == 0:
                    output[i] = chr(65 + i) 
                else:
                    output[hashMap[i][1]] = hashMap[i][0]
            return ''.join(output)
        
        if char == '?':
            count += 1
        else:
            hashMap[ord(char) % 65] = (char,i)
    return -1

print(checkWord(words))
