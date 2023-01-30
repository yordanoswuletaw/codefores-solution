n = int(input())

for _ in range(n):
    hashMap = {}
    wordLen = int(input())
    word1 = list(input().split())
    word2 = list(input().split())
    word3 = list(input().split())

    for i in range(wordLen):
        hashMap[word1[i]] = hashMap.get(word1[i], 0) + 1
        hashMap[word2[i]] = hashMap.get(word2[i], 0) + 1
        hashMap[word3[i]] = hashMap.get(word3[i], 0) + 1

    res1 = res2 = res3 = 0
    for i in range(wordLen):
        if hashMap[word1[i]] == 2 or hashMap[word1[i]] == 1:
            res1 += 3 // hashMap[word1[i]]
        if hashMap[word2[i]] == 2 or hashMap[word2[i]] == 1:
            res2 += 3 // hashMap[word2[i]]
        if hashMap[word3[i]] == 2 or hashMap[word3[i]] == 1:
            res3 += 3 // hashMap[word3[i]]
        
    print(res1, res2, res3)
    