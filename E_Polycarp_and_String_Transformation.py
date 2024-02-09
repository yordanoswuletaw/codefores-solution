from collections import defaultdict
def main():
    for _ in range(int(input())):
        strs = list(input())
        freq = defaultdict(lambda: (0, 0))

        for i in range(len(strs)):
            freq[strs[i]]  = (i, freq[strs[i]][1] + 1)
        
        order = []
        for val, key in sorted([(val, key) for key, val in freq.items()]):
            order.append(key)
        
        target = {}
        for i, ltr in enumerate(order):
            target[ltr] = freq[ltr][1] / (i + 1)
        
        window = defaultdict(float)
        ans = -1
        lastIndx = 0
        for i in range(len(strs)):
            window[strs[i]] += 1
            if window == target:
                ans = strs[:i + 1]
                lastIndx = i + 1
                break
        
        if ans != -1:
            currans = ans
            for char in order:
                next = []
                for each in currans:
                    if each != char:
                        next.append(each)
                if next != strs[lastIndx : lastIndx + len(next)]:
                    ans = -1
                lastIndx += len(next)
                currans = next
                if ans == -1:
                    break
        
        if ans != -1:
            print(''.join(ans), ''.join(order))
        else:
            print(-1)

if __name__ == '__main__':
    main()