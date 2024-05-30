def main():
    n, m, c = map(int, input().split())
    msgs = list(map(int, input().split()))
    encKeys = [0] + list(map(int, input().split()))

    # perform a prefix sum over enceryption keys
    for i in range(1, m + 1):
        encKeys[i] += encKeys[i - 1]
    # decrypt the messages
    for i, msg in enumerate(msgs):
        right = min(i + 1, m)
        left = max(0, m - (n - i))
    
        msgs[i] = (msg + encKeys[right] - encKeys[left]) % c
    
    print(*msgs)

if __name__ == '__main__':
    main()