def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    sfxSum = [nums[-1]]
    for i in range(n - 2, -1, -1):
        sfxSum.append(sfxSum[-1] + nums[i])
    
    ans = sfxSum.pop()
    sfxSum.sort(reverse=True)
    for i in range(k - 1):
        ans += sfxSum[i]
    print(ans)

if __name__ == '__main__':
    main()

