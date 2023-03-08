from collections import Counter
import string

word = list(input())
n = len(word)

def check(word, n):
    substr = Counter(word[:26])
    repeated = 0
    for char in substr:
        if char != '?' and substr[char] > 1:
            repeated += 1
    if repeated == 0:
        return populate(0)
    for i in range(1, n - 26 + 1):
        nxtWord = word[i + 26 - 1]
        substr[nxtWord]  += 1
        if nxtWord != '?' and substr[nxtWord] == 2:
            repeated += 1

        prev = word[i - 1]
        substr[prev] -= 1
        if prev != '?' and substr[prev] == 1:
            repeated -= 1  
        
        if repeated == 0:
            return populate(i)
        
    return -1


def populate(i):
    used = set(word[i:i + 26])
    used.discard('?')
    missed = set(string.ascii_uppercase) - used 
    for i in range(i, i+26):
        if word[i] == '?':
            word[i] = missed.pop()
    return ''.join(word).replace('?','Y')


if n < 26:
    print(-1)
    exit(0)

print(check(word, n))

