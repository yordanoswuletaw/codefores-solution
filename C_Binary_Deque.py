def main():
    for _ in range(int(input())):
        n, s = map(int, input().split())
        nums = list(map(int, input().split()))
        totSum = sum(nums)
        if totSum < s:
            print(-1)
        elif totSum == s:
            print(0)
        else:
            left, right = [], []
            for i in range(n):
                if nums[i]:
                    left.append(i)
            for i in range(n - 1, -1, -1):
                if nums[i]:
                    right.append(n - 1 - i)
            
            ops = 0 
            n, m = len(left), len(right)
            i, previ = 0, -1
            j, prevj = 0, -1
            while (i < n or j < m) and totSum > s:
                if i < n and j < m:
                    if left[i] - previ <= right[j] - prevj:
                        ops += left[i] - previ
                        previ, i = left[i], i + 1
                    else:
                        ops += right[j] - prevj
                        prevj, j = right[j], j + 1
                    totSum -= 1
                elif i < n:
                    ops += left[i] - previ
                    previ, i = left[i], i + 1
                    totSum -= 1
                elif j < m:
                    ops += right[j] - prevj
                    prevj, j = right[j], j + 1
                    totSum -= 1
            print(ops)

if __name__ == '__main__':
    main()