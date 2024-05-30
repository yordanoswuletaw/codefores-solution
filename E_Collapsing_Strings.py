class TrieNode:
    def __init__(self):
        self.ch = {}
        self.freq = 0 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        trie = self.root
        for ltr in word:
            if ltr not in trie.ch:
                trie.ch[ltr] = TrieNode()
            trie = trie.ch[ltr]
            trie.freq += 1

def main():
    n = int(input())    
    words = []
    for _ in range(n):
        words.append(input())
        
    trie = Trie()
    tot = 0
    for word in words:
        tot += len(word)
        trie.insert(word)
    ans = 0
    for word in words:
        curr = trie.root
        curr_tot = tot + (n * len(word))
        for i in range(len(word) - 1, -1, -1):
            ltr = word[i]
            if ltr not in curr.ch:
                break
            curr = curr.ch[ltr]
            curr_tot -= 2 * curr.freq
        ans += curr_tot
    
    print(ans)

if __name__ == '__main__':
    main()
 
 