def main():
    n = int(input())
    stones = list(map(int, input().split()))
    orderedStones = sorted(stones)

    prfxSum1 = [0]
    prfxSum2 = [0]
    for i in range(n):
        prfxSum1.append(prfxSum1[-1] + stones[i])
        prfxSum2.append(prfxSum2[-1] + orderedStones[i])

    m = int(input())

    questions = []
    for _ in range(m):
        questions.append(list(map(int, input().split())))
    
    for q in questions:
        if q[0] == 2:
            print(prfxSum2[q[2]] - prfxSum2[q[1] - 1]) 
        else:
            print(prfxSum1[q[2]] - prfxSum1[q[1] - 1 ])    

if __name__ == '__main__':
    main()

