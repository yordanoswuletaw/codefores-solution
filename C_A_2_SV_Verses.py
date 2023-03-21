












n, a, b = map(int, input().split())
solved = sorted(map(int, input().split()), reverse=True)

j, i = 0, n - 1
eligible = 0
while j < n and a <= solved[j] <= b:
    eligible += 1
    j += 1
solvedSum = 0
while j < i:
    solvedSum += solved[i] + solved[j]
    if a <= solvedSum <= b:
        eligible += 1
        solvedSum = 0 
        j += 1
    else:
        solvedSum -= solved[i]
    i -= 1

print(eligible)