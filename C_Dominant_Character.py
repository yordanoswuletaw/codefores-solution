for _ in range(int(input())):
    n = int(input())
    string = input()
    ans = float("inf")
    validStrings = {"aa", "aba", "aca", "abca", "acba", "abbacca", "accabba"}
    for valid in validStrings:
        if valid in string:
            ans = min(ans, len(valid))
            
    print(-1 if ans == float("inf") else ans)