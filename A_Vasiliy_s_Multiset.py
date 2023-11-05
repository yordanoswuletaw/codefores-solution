from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.bits = [None] * 2
        self.count = 0
    
def add(trie, num):
    for i in range(31, -1, -1):
        bit = int(bool(num & (1 << i)))
        if not trie.bits[bit]:
            trie.bits[bit] = TrieNode()
        trie = trie.bits[bit]
        trie.count += 1

def remove(trie, num):
    for i in range(31, -1, -1):
        bit = int(bool(num & (1 << i)))
        nxt = trie.bits[bit]
        nxt.count -= 1
        if nxt.count <= 0:
            trie.bits[bit] = None
        trie = nxt 
    
def findXOR(trie, num):
    output = 0
    for i in range(31, -1, -1):
        bit = int(bool(num & (1 << i)))
        if bit == 0 and trie.bits[1]:
            output |= (1 << i)
            trie = trie.bits[1]
        elif bit == 1 and trie.bits[0]:
            trie = trie.bits[0]
        else:
            output |= (bit << i)
            trie = trie.bits[bit]
            
    return output ^ num

def main():
    n = int(input())
    trie = TrieNode()
    add(trie, 0)
    for _ in range(n):
        cmd, num = input().split()
        if cmd == '+':
            add(trie, int(num))
        elif cmd == '-':
            remove(trie, int(num))
        else: 
            ans = 0
            ans = max(ans, findXOR(trie, int(num)))
            print(ans) 

if __name__ == '__main__':
    main()