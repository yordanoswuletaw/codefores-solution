def solution(quantity, queries):
    n, q = len(quantity), queries
    ans = []
    for query in queries:
        left, right = 0, n - 1
        req = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            if quantity[mid] >= query:
                req = min(mid + 1, req)
                right = mid - 1
            else:
                left = mid + 1
       
        ans.append(-1) if req == float('inf') else ans.append(req)

    return ans

def main():
    for _ in range(int(input())):
        n, q = map(int, input().split())
        quantity = sorted(map(int, input().split()), reverse=True)
        for i in range(1, n):
            quantity[i] += quantity[i - 1]
        queries = []
        for _ in range(q):
            queries.append(int(input()))

        for each in (solution(quantity, queries) ):
            print(each)

if __name__ == '__main__':
    main()